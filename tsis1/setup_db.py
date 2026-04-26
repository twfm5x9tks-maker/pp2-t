# setup_db.py
import psycopg2
from config import config

def setup_database():
    """Initialize database with all extensions"""
    # Connect to default postgres database first
    conn = psycopg2.connect(
        dbname='postgres',
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        port=config.DB_PORT
    )
    conn.autocommit = True
    
    with conn.cursor() as cur:
        # Create database if not exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{config.DB_NAME}'")
        if not cur.fetchone():
            cur.execute(f"CREATE DATABASE {config.DB_NAME}")
            print(f"Database {config.DB_NAME} created")
    
    conn.close()
    
    # Connect to new database
    conn = psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        port=config.DB_PORT
    )
    conn.autocommit = True
    
    with conn.cursor() as cur:
        # Execute schema
        with open('schema.sql', 'r') as f:
            cur.execute(f.read())
        print("Schema created")
        
        # Execute procedures
        with open('procedures.sql', 'r') as f:
            cur.execute(f.read())
        print("Procedures created")
    
    conn.close()
    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()