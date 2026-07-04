# === Stage 20: Добавь восстановление записей из архива ===
# Project: MiniCRM
import json, os, sys
from datetime import datetime

def restore_from_archive():
    archive_path = "archive.json"
    if not os.path.exists(archive_path):
        return
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for record in data.get("contacts", []):
            print(f"Restored contact {record['id']}")
        for deal in data.get("deals", []):
            print(f"Restored deal {deal['id']}")
    except Exception as e:
        print(f"Error restoring archive: {e}")

if __name__ == "__main__":
    restore_from_archive()
