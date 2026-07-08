# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MiniCRM
def check_overdue_reminders():
    """Проверяет просроченные напоминания и выводит список."""
    overdue = []
    for item in reminders:
        if isinstance(item, Reminder):
            if hasattr(item, 'deadline') and item.deadline is not None and item.done is False:
                from datetime import datetime
                if datetime.now() > item.deadline:
                    overdue.append(item)
    return overdue
