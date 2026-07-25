# === Stage 32: Добавь журнал действий пользователя ===
# Project: MiniCRM
import datetime, hashlib, json

class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, actor, action_type, detail=""):
        entry = {
            "id": len(self.entries) + 1,
            "timestamp": datetime.datetime.now().isoformat(),
            "actor": actor,
            "action_type": action_type,
            "detail": detail
        }
        self.entries.append(entry)

    def get_log(self):
        return self.entries

    def display_log(self, max_entries=10):
        entries = self.entries[-max_entries:] if len(self.entries) > max_entries else self.entries
        for e in reversed(entries):
            print(f"#{e['id']} | {e['timestamp'][:16]} | {e['actor']:8} | {e['action_type']:20} | {e['detail']}")

    def to_json(self, filepath="action_log.json"):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump({"actions": self.entries}, f, ensure_ascii=False, indent=2)

    @classmethod
    def from_json(cls, filepath="action_log.json"):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            log = cls()
            log.entries = data.get("actions", [])
            return log
        except FileNotFoundError:
            return cls()

    def clear(self):
        self.entries.clear()
