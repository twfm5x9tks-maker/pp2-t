# connect.py
import psycopg2
from config import config

def get_connection():
    """Create and return database connection"""
    try:
        conn = psycopg2.connect(**config.DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def execute_query(query, params=None, fetch=False):
    """Execute query and optionally fetch results"""
    conn = get_connection()
    if not conn:
        return None if not fetch else []
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetch:
                result = cur.fetchall()
                conn.commit()
                return result
            conn.commit()
            return True
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return None if not fetch else []
    finally:
        conn.close()