import psycopg2
from config import DB_CONFIG

def connect():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL UNIQUE
                )
            """)
    print("Таблица готова")

def add_contact(username, phone):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                    (username, phone)
                )
        print(f"✓ {username} добавлен")
    except psycopg2.errors.UniqueViolation:
        print(f"Ошибка: {phone} уже существует")

def add_contact_from_console():
    username = input("Введите имя: ")
    phone = input("Введите телефон: ")
    add_contact(username, phone)

def import_from_csv(filename):
    import csv
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # пропустить заголовок
            for row in reader:
                if len(row) >= 2:
                    add_contact(row[0], row[1])
        print("Импорт завершен")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

def search_contacts():
    keyword = input("Введите имя или телефон для поиска: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM phonebook 
                WHERE username ILIKE %s OR phone ILIKE %s
            """, (f"%{keyword}%", f"%{keyword}%"))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено")
            else:
                for row in rows:
                    print(f"{row[0]}. {row[1]} - {row[2]}")

def update_contact():
    contact_id = input("Введите ID контакта для обновления: ")
    field = input("Что обновить? (name/phone): ").lower()
    new_value = input("Введите новое значение: ")
    
    with connect() as conn:
        with conn.cursor() as cur:
            if field == 'name':
                cur.execute("UPDATE phonebook SET username = %s WHERE id = %s", (new_value, contact_id))
            elif field == 'phone':
                cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (new_value, contact_id))
            else:
                print("Неверное поле")
                return
        print("✓ Контакт обновлен")

def delete_contact():
    contact_id = input("Введите ID контакта для удаления: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE id = %s", (contact_id,))
        print("✓ Контакт удален")

def show_contacts():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY id")
            rows = cur.fetchall()
            if not rows:
                print("Нет контактов")
            else:
                print("\n=== Мои контакты ===")
                for row in rows:
                    print(f"{row[0]}. {row[1]} - {row[2]}")
                print()

def menu():
    while True:
        print("\n=== PHONEBOOK MENU ===")
        print("1. Показать все контакты")
        print("2. Добавить контакт (вручную)")
        print("3. Импорт из CSV")
        print("4. Поиск контакта")
        print("5. Обновить контакт")
        print("6. Удалить контакт")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            show_contacts()
        elif choice == '2':
            add_contact_from_console()
        elif choice == '3':
            filename = input("Введите имя CSV файла: ")
            import_from_csv(filename)
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            show_contacts()
            update_contact()
        elif choice == '6':
            show_contacts()
            delete_contact()
        elif choice == '7':
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    create_table()
    menu()