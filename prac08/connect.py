import sqlite3

DB_FILE = "phonebook.db"

def get_connection():
    """Create and return database connection"""
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def test_connection():
    """Test if connection works"""
    conn = get_connection()
    if conn:
        print("✓ Database connection successful!")
        conn.close()
        return True
    else:
        print("✗ Database connection failed!")
        return False

def close_connection(conn):
    """Close database connection"""
    if conn:
        conn.close()