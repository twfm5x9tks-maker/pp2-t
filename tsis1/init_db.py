# init_db.py
import psycopg2
from config import config

conn = psycopg2.connect(**config.DB_CONFIG)
conn.autocommit = True
cur = conn.cursor()

# Создаем таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
    
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL,
        email VARCHAR(100),
        birthday DATE,
        group_id INTEGER REFERENCES groups(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS phones (
        id SERIAL PRIMARY KEY,
        contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
        phone VARCHAR(20) NOT NULL,
        type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
    );
""")

# Добавляем группы
cur.execute("""
    INSERT INTO groups (name) VALUES 
        ('Family'), ('Work'), ('Friend'), ('Other')
    ON CONFLICT (name) DO NOTHING;
""")

print("✓ Таблицы созданы!")
cur.close()
conn.close()