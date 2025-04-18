import re

def log_analyser():
    # Expression régulière corrigée
    pattern = re.compile(
        r"^(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) .* Failed password for (?:invalid user )?(\w+) from ([\d\.]+)"
    )

    # Lecture du fichier log
    with open("system_automation/src/data/auth.log") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ts, user, ip = match.groups()
                print(f"{ts} - Failed login by {user} from {ip}")
