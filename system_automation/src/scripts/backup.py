from datetime import datetime
import shutil
import os

def backup():
    timestamp = datetime.now().strftime("%Y%m%d")

    archive_dir = "system_automation/src/archive"
    archive_name = f"backup_{timestamp}"
    archive_path = os.path.join(archive_dir, archive_name)

    os.makedirs(archive_dir, exist_ok=True)

    shutil.make_archive(archive_path, "zip", root_dir="system_automation/src/")

    print(f"Archive créée : {archive_path}.zip")