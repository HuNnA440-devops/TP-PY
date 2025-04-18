import sqlite3
import csv

def csv_to_db():

    conn = sqlite3.connect("system_automation/src/db/users.db")
    c = conn.cursor()


    c.execute("DROP TABLE IF EXISTS users")
    c.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    login_attempts INTEGER,
    last_login DATE
)
""")

    with open("system_automation/src/data/users.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            c.execute("""
        INSERT INTO users (user_id, username, email, login_attempts, last_login)
        VALUES (?, ?, ?, ?, ?)
        """, (
            int(row['user_id']),
            row['username'],
            row['email'],
            int(row['login_attempts']),
            row['last_login'].strip()
        ))


    conn.commit()
    conn.close()
