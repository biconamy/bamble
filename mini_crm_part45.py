# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MiniCRM
import json, os

def load_backup(path="backup.json"):
    if not os.path.exists(path):
        print("Резервная копия не найдена.")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def restore_from_backup(backup_data):
    if not backup_data:
        print("Нет данных для восстановления.")
        return
    for key in ["contacts", "deals", "reminders", "history"]:
        if key in backup_data:
            globals()[key] = backup_data[key]
    print("CRM успешно восстановлена из резервной копии.")
