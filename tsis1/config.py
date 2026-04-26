# config.py
class Config:
    DB_CONFIG = {
        "dbname": "phonebook_db",
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": "5432"
    }
    
    PAGE_SIZE = 5
    EXPORT_FILE = "contacts_export.json"
    CSV_FILE = "contacts.csv"

config = Config()