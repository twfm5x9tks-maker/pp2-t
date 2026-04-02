import sqlite3
import csv
import os

DB_NAME = 'phonebook.db'

def get_connection():
    """Connect to database"""
    return sqlite3.connect(DB_NAME)

def create_table():
    """Create contacts table"""
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

def import_from_csv(filename):
    """Import contacts from CSV file"""
    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    count = 0
    errors = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    name, phone = row[0].strip(), row[1].strip()
                    try:
                        cursor.execute(
                            "INSERT INTO contacts (name, phone) VALUES (?, ?)",
                            (name, phone)
                        )
                        count += 1
                    except sqlite3.IntegrityError:
                        print(f"  {name} - phone already exists: {phone}")
                        errors += 1
        conn.commit()
        print(f"Imported {count} contacts, {errors} errors")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def show_all_contacts():
    """Show all contacts"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM contacts ORDER BY name")
    results = cursor.fetchall()
    conn.close()
    
    if results:
        print("\n" + "="*50)
        print("ALL CONTACTS")
        print("="*50)
        for row in results:
            print(f"  {row[0]}. {row[1]} - {row[2]}")
        print("="*50)
    else:
        print("\nPhonebook is empty")

def add_contact():
    """Add new contact"""
    print("\n--- ADD NEW CONTACT ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    
    if not name or not phone:
        print("Name and phone cannot be empty")
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO contacts (name, phone) VALUES (?, ?)",
            (name, phone)
        )
        conn.commit()
        print(f"'{name}' added successfully")
    except sqlite3.IntegrityError:
        print(f"Phone {phone} already exists")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def search_contacts():
    """Search contacts by name or phone"""
    search = input("\nSearch by name or phone: ").strip()
    
    if not search:
        print("Please enter search term")
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, phone FROM contacts 
        WHERE name LIKE ? OR phone LIKE ?
        ORDER BY name
    """, (f'%{search}%', f'%{search}%'))
    results = cursor.fetchall()
    conn.close()
    
    if results:
        print(f"\nFound {len(results)} contact(s):")
        print("-"*40)
        for row in results:
            print(f"  {row[0]}. {row[1]} - {row[2]}")
    else:
        print("No contacts found")

def update_contact():
    """Update contact"""
    show_all_contacts()
    
    contact_id = input("\nEnter contact ID to update: ").strip()
    
    if not contact_id.isdigit():
        print("ID must be a number")
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, phone FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()
    
    if not contact:
        print(f"Contact with ID {contact_id} not found")
        conn.close()
        return
    
    print(f"\nCurrent: {contact[0]} - {contact[1]}")
    new_name = input("New name (Enter to skip): ").strip()
    new_phone = input("New phone (Enter to skip): ").strip()
    
    if not new_name and not new_phone:
        print("No changes made")
        conn.close()
        return
    
    updates = []
    params = []
    if new_name:
        updates.append("name = ?")
        params.append(new_name)
    if new_phone:
        updates.append("phone = ?")
        params.append(new_phone)
    params.append(contact_id)
    
    try:
        query = f"UPDATE contacts SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        conn.commit()
        print("Contact updated successfully")
    except sqlite3.IntegrityError:
        print(f"Phone {new_phone} already exists")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def delete_contact():
    """Delete contact"""
    print("\n--- DELETE CONTACT ---")
    print("1. Delete by ID")
    print("2. Delete by Name")
    print("3. Delete by Phone")
    
    choice = input("Choose (1-3): ").strip()
    
    conn = get_connection()
    cursor = conn.cursor()
    
    if choice == '1':
        show_all_contacts()
        contact_id = input("Enter ID: ").strip()
        if not contact_id.isdigit():
            print("ID must be a number")
            conn.close()
            return
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        
    elif choice == '2':
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty")
            conn.close()
            return
        cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        
    elif choice == '3':
        phone = input("Enter phone: ").strip()
        if not phone:
            print("Phone cannot be empty")
            conn.close()
            return
        cursor.execute("DELETE FROM contacts WHERE phone = ?", (phone,))
        
    else:
        print("Invalid choice")
        conn.close()
        return
    
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    
    if deleted > 0:
        print(f"{deleted} contact(s) deleted")
    else:
        print("Contact not found")

def main_menu():
    """Main menu"""
    create_table()
    
    while True:
        print("\n" + "="*50)
        print("PHONEBOOK".center(45))
        print("="*50)
        print("  1. Show all contacts")
        print("  2. Add new contact")
        print("  3. Search contacts")
        print("  4. Update contact")
        print("  5. Delete contact")
        print("  6. Import from CSV")
        print("  0. Exit")
        print("-"*50)
        
        choice = input("Your choice (0-6): ").strip()
        
        if choice == '1':
            show_all_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            filename = input("CSV filename (e.g., contacts.csv): ").strip()
            import_from_csv(filename)
        elif choice == '0':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please enter 0-6")

if __name__ == "__main__":
    main_menu()