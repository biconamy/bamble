# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MiniCRM
class Reminder:
    def __init__(self, text, due_date):
        self.text = text
        self.due_date = due_date
        self.status = "pending" if isinstance(due_date, datetime) and due_date > datetime.now() else "overdue"

    @property
    def is_overdue(self):
        return self.status == "overdue"
    
    def __str__(self):
        label = "Просроченный" if self.is_overdue else "Активный"
        return f"[{label}] {self.text} (до: {self.due_date})"


class ReminderManager:
    def __init__(self):
        self.reminders = []
    
    def add(self, text, due_date):
        reminder = Reminder(text, due_date)
        self.reminders.append(reminder)
        return reminder
    
    def check_due(self):
        now = datetime.now()
        for r in self.reminders:
            if isinstance(r.due_date, datetime) and r.due_date <= now and r.status == "pending":
                r.status = "overdue"
        overdue = [r for r in self.reminders if r.is_overdue]
        return overdue
    
    def __str__(self):
        active = [r for r in self.reminders if not r.is_overdue]
        overdue = [r for r in self.reminders if r.is_overdue]
        result = f"Напоминания: {len(self.reminders)} всего ({len(active)} активных, {len(overdue)} просроченных)\n"
        for r in active + overdue:
            result += str(r) + "\n"
        return result
