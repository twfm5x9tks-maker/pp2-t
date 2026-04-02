import sqlite3
from config import DB_FILE

def get_connection():
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Exception as e:
        print(f"Connection error: {e}")
        return None