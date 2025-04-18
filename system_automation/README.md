System Automation Scripts

This repository contains a set of Python scripts designed to automate various system tasks. The scripts include functionalities for importing user data into a database, analyzing authentication logs, and backing up data files.


Scripts Overview :

main.py: The main script that orchestrates the execution of other scripts. It sequentially calls functions to import user data into a database, analyze authentication logs, and back up data files.

csv_to_db.py: This script connects to an SQLite database, creates a 'users' table, and populates it with data from a CSV file. The table includes columns for user ID, username, email, login attempts, and last login date.

log_analyzer.py: This script uses regular expressions to parse the 'auth.log' file. It extracts timestamps, usernames, and IP addresses from lines indicating failed login attempts and prints this information in a formatted string.

backup.py: This script creates a timestamped archive of the 'system_automation/src/' directory. It generates a ZIP file named with the current date in the 'system_automation/src/archive/' directory and prints a confirmation message.


Data Files :

users.csv: A CSV file containing user records with details including user ID, username, email, login attempts, and last login date.

auth.log: A log file containing SSH login attempts to a server, including both successful and failed password attempts.


Usage :

To use these scripts, follow these steps:

Ensure you have Python installed on your system.

Clone this repository to your local machine.

Install the required dependencies (if any) by running:

pip install -r requirements.txt

Run the main script:

python main.py


Author : 

Nolan Deruelle, Précieux Juste Bitemo, Éric Kim
