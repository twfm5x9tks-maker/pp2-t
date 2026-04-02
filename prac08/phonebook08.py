import sqlite3

DB_NAME = 'phonebook.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
    print("Database ready")

def search_contacts_pattern(pattern):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, phone FROM contacts 
        WHERE name LIKE ? OR phone LIKE ?
        ORDER BY name
    """, (f'%{pattern}%', f'%{pattern}%'))
    results = cursor.fetchall()
    conn.close()
    return results

def upsert_contact(name, phone):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM contacts WHERE name = ?", (name,))
    exists = cursor.fetchone()
    
    if exists:
        cursor.execute("UPDATE contacts SET phone = ? WHERE name = ?", (phone, name))
        result = f"Updated: {name}"
    else:
        try:
            cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
            result = f"Inserted: {name}"
        except sqlite3.IntegrityError:
            result = f"Phone {phone} already exists"
    
    conn.commit()
    conn.close()
    return result

def bulk_insert_contacts(contacts_list):
    conn = get_connection()
    cursor = conn.cursor()
    inserted = 0
    invalid = []
    
    for name, phone in contacts_list:
        if phone.isdigit() and 10 <= len(phone) <= 15:
            try:
                cursor.execute(
                    "INSERT INTO contacts (name, phone) VALUES (?, ?)",
                    (name, phone)
                )
                inserted += 1
            except sqlite3.IntegrityError:
                invalid.append((name, phone, "Phone already exists"))
        else:
            invalid.append((name, phone, "Invalid phone format"))
    
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted} contacts")
    return invalid

def get_contacts_paginated(page_num, rows_per_page):
    conn = get_connection()
    cursor = conn.cursor()
    
    offset = (page_num - 1) * rows_per_page
    cursor.execute("""
        SELECT id, name, phone FROM contacts 
        ORDER BY id
        LIMIT ? OFFSET ?
    """, (rows_per_page, offset))
    
    results = cursor.fetchall()
    conn.close()
    return results

def delete_contact_by(identifier, delete_type):
    conn = get_connection()
    cursor = conn.cursor()
    
    if delete_type == 'name':
        cursor.execute("DELETE FROM contacts WHERE name = ?", (identifier,))
    elif delete_type == 'phone':
        cursor.execute("DELETE FROM contacts WHERE phone = ?", (identifier,))
    else:
        conn.close()
        return False, "Invalid type"
    
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    
    if deleted > 0:
        return True, f"Deleted {deleted} contact(s)"
    else:
        return False, f"No contact found"

def show_all_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM contacts ORDER BY name")
    results = cursor.fetchall()
    conn.close()
    
    if results:
        print("\nALL CONTACTS:")
        for row in results:
            print(f"  {row[0]}. {row[1]} - {row[2]}")
    else:
        print("Phonebook is empty")

def add_sample_data():
    sample = [
        ("Alice Johnson", "77011234567"),
        ("Bob Smith", "77017654321"),
        ("Charlie Brown", "77019876543"),
        ("Diana Prince", "77015556677"),
        ("Eve Wilson", "77019998888")
    ]
    print("Adding sample data...")
    bulk_insert_contacts(sample)

def main():
    create_table()
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM contacts")
    count = cursor.fetchone()[0]
    conn.close()
    
    if count == 0:
        add_sample_data()
    
    while True:
        print("\n" + "="*50)
        print("PRACTICE 8 - PHONEBOOK")
        print("="*50)
        print("1. Show all contacts")
        print("2. Pattern search")
        print("3. Upsert contact")
        print("4. Bulk insert")
        print("5. Paginated query")
        print("6. Delete contact")
        print("0. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            show_all_contacts()
        elif choice == '2':
            p = input("Pattern: ")
            results = search_contacts_pattern(p)
            for r in results:
                print(f"  {r[1]} - {r[2]}")
        elif choice == '3':
            n = input("Name: ")
            p = input("Phone: ")
            print(upsert_contact(n, p))
        elif choice == '4':
            contacts = []
            while True:
                n = input("Name (done to stop): ")
                if n == 'done':
                    break
                p = input("Phone: ")
                contacts.append((n, p))
            bulk_insert_contacts(contacts)
        elif choice == '5':
            page = int(input("Page: "))
            per = int(input("Per page: "))
            results = get_contacts_paginated(page, per)
            for r in results:
                print(f"  {r[1]} - {r[2]}")
        elif choice == '6':
            t = input("Delete by (name/phone): ")
            v = input("Value: ")
            success, msg = delete_contact_by(v, t)
            print(msg)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()