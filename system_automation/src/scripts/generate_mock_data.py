# scripts/generate_mock_data.py

from faker import Faker
import csv
import random
import os
from datetime import datetime

fake = Faker()
os.makedirs("system_automation/src/data", exist_ok=True)

# Generate users.csv
with open("system_automation/src/data/users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "username", "email", "login_attempts", "last_login"])

    for uid in range(1, 21):
        username = fake.user_name()
        email = fake.email()
        attempts = random.randint(0, 15)
        last_login = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([uid, username, email, attempts, last_login])

# Generate auth.log
with open("system_automation/src/data/auth.log", "w") as f:
    for _ in range(100):
        date = fake.date_time_this_year().strftime("%b %d %H:%M:%S")
        user = fake.user_name()
        ip = fake.ipv4()
        success = random.choice([True, False])
        if success:
            line = f"{date} server sshd[12345]: Accepted password for user {user} from {ip}\n"
        else:
            line = f"{date} server sshd[12345]: Failed password for user {user} from {ip}\n"
        f.write(line)
