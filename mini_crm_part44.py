# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MiniCRM
import datetime
import json
import os
import shutil
import tempfile

def backup_data_file(db_file, backup_dir=None):
    if backup_dir is None:
        backup_dir = tempfile.gettempdir()
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, "minicrm_backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".json")
    with open(db_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return backup_path

def restore_data_file(backup_file, original_db_file):
    with open(backup_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(original_db_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Данные восстановлены из: {backup_file}")
