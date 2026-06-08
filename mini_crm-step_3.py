# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MiniCRM
contacts = {}
deals = {}
reminders = []
history = []

def add_contact(name, phone, email=None):
    if name not in contacts:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Контакт {name} добавлен.")
    else:
        print(f"Контакт {name} уже существует.")

def add_deal(client_name, amount, stage="new"):
    if client_name not in deals:
        deals[client_name] = {"amount": amount, "stage": stage}
        print(f"Сделка с {client_name} на сумму {amount} добавлена.")
    else:
        print(f"Сделка с {client_name} уже существует.")

def add_reminder(text, date):
    reminders.append({"text": text, "date": date})
    print(f"Напоминание '{text}' добавлено на {date}.")

def log_interaction(client_name, message):
    history.append({"client": client_name, "message": message, "timestamp": time.time()})
    print(f"Взаимодействие с {client_name} записано.")
