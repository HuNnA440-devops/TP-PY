# system_automation/src/main.py
from src.scripts.log_analyzer import log_analizer
from src.scripts.csv_to_db import csv_to_db
from src.scripts.backup import backup

def main():

    print("Import users into the database...")
    csv_to_db()

    print("Log analysis auth.log...")
    log_analizer()

    print("backup data files")
    backup()

if __name__ == "__main__":
    main()

