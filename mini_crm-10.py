# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MiniCRM
def export_to_json():
    import json
    data = {
        "contacts": contacts,
        "deals": deals,
        "reminders": reminders,
        "history": history
    }
    return json.dumps(data, indent=2)
