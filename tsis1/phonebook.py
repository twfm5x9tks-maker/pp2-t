# phonebook.py
import psycopg2
import json
import csv
from config import config
from connect import get_connection

class PhoneBook:
    def __init__(self):
        self.page = 1
        self.page_size = 5
        self.sort_by = "name"
        self.group_filter = None
        self.conn = None

    def get_conn(self):
        return get_connection()

    def show_all(self):
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT c.id, c.name, c.phone, c.email, c.birthday, g.name
                    FROM contacts c LEFT JOIN groups g ON c.group_id = g.id
                    ORDER BY c.name
                """)
                rows = cur.fetchall()
                if rows:
                    print("\n" + "="*50)
                    print("ALL CONTACTS")
                    print("="*50)
                    for r in rows:
                        print(f"{r[0]}. {r[1]} - {r[2]}")
                        if r[3]: print(f"   Email: {r[3]}")
                        if r[4]: print(f"   Birthday: {r[4]}")
                        if r[5]: print(f"   Group: {r[5]}")
                        print("-"*40)
                else:
                    print("\nPhonebook is empty")
        finally:
            conn.close()

    def add(self):
        print("\n--- ADD CONTACT ---")
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email (optional): ").strip() or None
        birthday = input("Birthday (YYYY-MM-DD, optional): ").strip() or None
        group = input("Group (Family/Work/Friend/Other, optional): ").strip() or None
        
        if not name or not phone:
            print("Name and phone required!")
            return
        
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                group_id = None
                if group:
                    cur.execute("SELECT id FROM groups WHERE name = %s", (group,))
                    res = cur.fetchone()
                    if res: group_id = res[0]
                cur.execute("""
                    INSERT INTO contacts (name, phone, email, birthday, group_id) 
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, phone, email, birthday, group_id))
                conn.commit()
                print(f"✓ '{name}' added")
        except psycopg2.IntegrityError:
            print(f"✗ Phone {phone} already exists")
            conn.rollback()
        finally:
            conn.close()

    def search_pattern(self):
        pattern = input("\nSearch pattern: ").strip()
        if not pattern: return
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT name, phone, email FROM contacts 
                    WHERE name ILIKE %s OR phone ILIKE %s
                """, (f'%{pattern}%', f'%{pattern}%'))
                rows = cur.fetchall()
                if rows:
                    print(f"\nFound {len(rows)} contact(s):")
                    for r in rows:
                        print(f"  {r[0]} - {r[1]}")
                        if r[2]: print(f"    Email: {r[2]}")
                else:
                    print("No contacts found")
        finally:
            conn.close()

    def update(self):
        self.show_all()
        cid = input("\nContact ID to update: ").strip()
        if not cid.isdigit():
            print("Invalid ID")
            return
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT name, phone FROM contacts WHERE id = %s", (cid,))
                contact = cur.fetchone()
                if not contact:
                    print("Contact not found")
                    return
                print(f"Current: {contact[0]} - {contact[1]}")
                new_name = input("New name (Enter to skip): ").strip()
                new_phone = input("New phone (Enter to skip): ").strip()
                if new_name:
                    cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, cid))
                if new_phone:
                    cur.execute("UPDATE contacts SET phone = %s WHERE id = %s", (new_phone, cid))
                conn.commit()
                print("✓ Contact updated")
        finally:
            conn.close()

    def delete(self):
        print("\n--- DELETE CONTACT ---")
        print("1. By ID\n2. By Name\n3. By Phone")
        choice = input("Choice (1-3): ").strip()
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                if choice == '1':
                    self.show_all()
                    cid = input("ID: ").strip()
                    if not cid.isdigit(): return
                    cur.execute("DELETE FROM contacts WHERE id = %s", (cid,))
                elif choice == '2':
                    name = input("Name: ").strip()
                    if not name: return
                    cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
                elif choice == '3':
                    phone = input("Phone: ").strip()
                    if not phone: return
                    cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
                else:
                    print("Invalid choice")
                    return
                conn.commit()
                print(f"✓ {cur.rowcount} contact(s) deleted")
        finally:
            conn.close()

    def paginated_view(self):
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                # Get total count
                count_q = "SELECT COUNT(*) FROM contacts c LEFT JOIN groups g ON c.group_id = g.id"
                if self.group_filter:
                    count_q += " WHERE g.name = %s"
                    cur.execute(count_q, (self.group_filter,))
                else:
                    cur.execute(count_q)
                total = cur.fetchone()[0]
                if total == 0:
                    print("\nNo contacts")
                    return
                
                total_pages = (total + self.page_size - 1) // self.page_size
                offset = (self.page - 1) * self.page_size
                
                order_clause = {"name": "c.name", "birthday": "c.birthday NULLS LAST", "created_at": "c.created_at"}.get(self.sort_by, "c.name")
                
                query = f"""
                    SELECT c.id, c.name, c.phone, c.email, c.birthday, g.name
                    FROM contacts c LEFT JOIN groups g ON c.group_id = g.id
                """
                if self.group_filter:
                    query += " WHERE g.name = %s"
                    query += f" ORDER BY {order_clause} LIMIT %s OFFSET %s"
                    cur.execute(query, (self.group_filter, self.page_size, offset))
                else:
                    query += f" ORDER BY {order_clause} LIMIT %s OFFSET %s"
                    cur.execute(query, (self.page_size, offset))
                
                rows = cur.fetchall()
                print(f"\n{'='*60}")
                print(f"Page {self.page}/{total_pages}")
                if self.group_filter: print(f"Filter: {self.group_filter}")
                print(f"Sort by: {self.sort_by}")
                print(f"{'='*60}")
                
                for r in rows:
                    print(f"\n{r[1]}\n  Phone: {r[2]}")
                    if r[3]: print(f"  Email: {r[3]}")
                    if r[4]: print(f"  Birthday: {r[4]}")
                    if r[5]: print(f"  Group: {r[5]}")
                    print("-"*40)
                
                print(f"\n[N]ext [P]rev [G]oto [Q]uit")
                cmd = input("Choice: ").lower()
                if cmd == 'n' and self.page < total_pages:
                    self.page += 1
                    self.paginated_view()
                elif cmd == 'p' and self.page > 1:
                    self.page -= 1
                    self.paginated_view()
                elif cmd == 'g':
                    try:
                        p = int(input("Page number: "))
                        if 1 <= p <= total_pages:
                            self.page = p
                            self.paginated_view()
                    except: pass
        finally:
            conn.close()

    def filter_group(self):
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT name FROM groups ORDER BY name")
                groups = cur.fetchall()
                print("\nGroups:")
                for i, g in enumerate(groups, 1):
                    print(f"  {i}. {g[0]}")
                print("  0. Clear filter")
                choice = input("Select: ").strip()
                if choice == '0':
                    self.group_filter = None
                elif choice.isdigit() and 1 <= int(choice) <= len(groups):
                    self.group_filter = groups[int(choice)-1][0]
                self.page = 1
                self.paginated_view()
        finally:
            conn.close()

    def search_email(self):
        pattern = input("\nEmail pattern (e.g., 'gmail'): ").strip()
        if not pattern: return
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT name, phone, email FROM contacts 
                    WHERE email ILIKE %s
                """, (f'%{pattern}%',))
                rows = cur.fetchall()
                if rows:
                    print(f"\nContacts with email containing '{pattern}':")
                    for r in rows:
                        print(f"  {r[0]} - {r[1]} ({r[2]})")
                else:
                    print("No contacts found")
        finally:
            conn.close()

    def sort_menu(self):
        print("\nSort by:\n1. Name\n2. Birthday\n3. Date added")
        choice = input("Choice: ").strip()
        if choice == '1':
            self.sort_by = "name"
        elif choice == '2':
            self.sort_by = "birthday"
        elif choice == '3':
            self.sort_by = "created_at"
        else:
            return
        self.page = 1
        print(f"✓ Sorting by {self.sort_by}")

    def add_phone_proc(self):
        name = input("Contact name: ").strip()
        phone = input("Phone number: ").strip()
        ptype = input("Type (home/work/mobile): ").strip()
        if ptype not in ['home', 'work', 'mobile']:
            print("Invalid type")
            return
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.callproc('add_phone', (name, phone, ptype))
                conn.commit()
                print(f"✓ Phone added to {name}")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            conn.close()

    def move_group_proc(self):
        name = input("Contact name: ").strip()
        group = input("Group name: ").strip()
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.callproc('move_to_group', (name, group))
                conn.commit()
                print(f"✓ {name} moved to {group}")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            conn.close()

    def advanced_search(self):
        query = input("\nSearch term: ").strip()
        if not query: return
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts(%s)", (query,))
                rows = cur.fetchall()
                if not rows:
                    print("No results")
                    return
                print(f"\nResults for '{query}':")
                for r in rows:
                    print(f"\nName: {r[0]}\nPhones: {r[1]}\nEmail: {r[2]}\nBirthday: {r[3]}\nGroup: {r[4]}")
                    print("-"*40)
        finally:
            conn.close()

    def export_json(self):
        conn = self.get_conn()
        if not conn: return
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT c.name, c.email, c.birthday, g.name,
                           COALESCE(json_agg(json_build_object('phone', p.phone, 'type', p.type)) FILTER (WHERE p.id IS NOT NULL), '[]')
                    FROM contacts c
                    LEFT JOIN phones p ON c.id = p.contact_id
                    LEFT JOIN groups g ON c.group_id = g.id
                    GROUP BY c.id, c.name, c.email, c.birthday, g.name
                """)
                data = [{"name": r[0], "email": r[1], "birthday": str(r[2]) if r[2] else None, "group": r[3], "phones": r[4]} for r in cur.fetchall()]
                with open("export.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"✓ Exported {len(data)} contacts")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def import_json(self):
        try:
            with open("export.json", "r", encoding="utf-8") as f:
                contacts = json.load(f)
        except FileNotFoundError:
            print("export.json not found")
            return
        conn = self.get_conn()
        if not conn: return
        imported = 0
        try:
            with conn.cursor() as cur:
                for c in contacts:
                    cur.execute("SELECT id FROM contacts WHERE name = %s", (c['name'],))
                    if cur.fetchone():
                        choice = input(f"{c['name']} exists. Overwrite? (y/n): ").lower()
                        if choice != 'y':
                            continue
                        cur.execute("DELETE FROM contacts WHERE name = %s", (c['name'],))
                    
                    group_id = None
                    if c.get('group'):
                        cur.execute("SELECT id FROM groups WHERE name = %s", (c['group'],))
                        g = cur.fetchone()
                        if g:
                            group_id = g[0]
                        else:
                            cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (c['group'],))
                            group_id = cur.fetchone()[0]
                    
                    cur.execute("INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
                              (c['name'], c.get('email'), c.get('birthday'), group_id))
                    cid = cur.fetchone()[0]
                    for p in c.get('phones', []):
                        cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", (cid, p['phone'], p['type']))
                    imported += 1
                conn.commit()
                print(f"✓ Imported {imported} contacts")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            conn.close()

    def import_csv(self):
        fname = input("CSV filename: ").strip()
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                contacts = list(reader)
        except FileNotFoundError:
            print("File not found")
            return
        conn = self.get_conn()
        if not conn: return
        imported = 0
        try:
            with conn.cursor() as cur:
                for c in contacts:
                    name = c.get('name', '').strip()
                    phone = c.get('phone', '').strip()
                    if not name or not phone:
                        continue
                    cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
                    if cur.fetchone():
                        continue
                    
                    group_id = None
                    if c.get('group'):
                        cur.execute("SELECT id FROM groups WHERE name = %s", (c['group'],))
                        g = cur.fetchone()
                        if g:
                            group_id = g[0]
                        else:
                            cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (c['group'],))
                            group_id = cur.fetchone()[0]
                    
                    cur.execute("INSERT INTO contacts (name, phone, email, birthday, group_id) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                              (name, phone, c.get('email'), c.get('birthday'), group_id))
                    cid = cur.fetchone()[0]
                    ptype = c.get('phone_type', 'mobile')
                    if ptype in ['home', 'work', 'mobile']:
                        cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", (cid, phone, ptype))
                    imported += 1
                conn.commit()
                print(f"✓ Imported {imported} contacts from CSV")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            conn.close()

    def run(self):
        while True:
            print("\n" + "="*50)
            print("PHONEBOOK - TSIS1".center(45))
            print("="*50)
            print("1. Show all")
            print("2. Add contact")
            print("3. Pattern search")
            print("4. Update contact")
            print("5. Delete contact")
            print("6. Paginated view")
            print("7. Filter by group")
            print("8. Search by email")
            print("9. Change sorting")
            print("10. Add phone (procedure)")
            print("11. Move to group (procedure)")
            print("12. Advanced search (function)")
            print("13. Export to JSON")
            print("14. Import from JSON")
            print("15. Import from CSV")
            print("0. Exit")
            print("-"*50)
            
            choice = input("Choice: ").strip()
            if choice == '1': self.show_all()
            elif choice == '2': self.add()
            elif choice == '3': self.search_pattern()
            elif choice == '4': self.update()
            elif choice == '5': self.delete()
            elif choice == '6': self.page = 1; self.paginated_view()
            elif choice == '7': self.filter_group()
            elif choice == '8': self.search_email()
            elif choice == '9': self.sort_menu()
            elif choice == '10': self.add_phone_proc()
            elif choice == '11': self.move_group_proc()
            elif choice == '12': self.advanced_search()
            elif choice == '13': self.export_json()
            elif choice == '14': self.import_json()
            elif choice == '15': self.import_csv()
            elif choice == '0': print("\nGoodbye!"); break
            else: print("Invalid choice")

if __name__ == "__main__":
    app = PhoneBook()
    app.run()