# fix_db.py
import psycopg2
from config import config

conn = psycopg2.connect(**config.DB_CONFIG)
conn.autocommit = True
cur = conn.cursor()

# Добавляем колонку group_id
try:
    cur.execute("ALTER TABLE contacts ADD COLUMN group_id INTEGER REFERENCES groups(id)")
    print("✓ Added group_id column")
except Exception as e:
    print(f"Note: {e}")

# Добавляем другие колонки если их нет
try:
    cur.execute("ALTER TABLE contacts ADD COLUMN email VARCHAR(100)")
    print("✓ Added email column")
except: pass

try:
    cur.execute("ALTER TABLE contacts ADD COLUMN birthday DATE")
    print("✓ Added birthday column")
except: pass

try:
    cur.execute("ALTER TABLE contacts ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    print("✓ Added created_at column")
except: pass

# Создаем таблицу groups если её нет
cur.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    )
""")
print("✓ Groups table ready")

# Добавляем группы
cur.execute("""
    INSERT INTO groups (name) VALUES ('Family'), ('Work'), ('Friend'), ('Other')
    ON CONFLICT (name) DO NOTHING
""")
print("✓ Default groups added")

# Создаем таблицу phones
cur.execute("""
    CREATE TABLE IF NOT EXISTS phones (
        id SERIAL PRIMARY KEY,
        contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
        phone VARCHAR(20) NOT NULL,
        type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
    )
""")
print("✓ Phones table ready")

cur.close()
conn.close()
print("\n✅ Database fixed! Now run: py phonebook.py")