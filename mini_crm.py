# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MiniCRM
import json
from datetime import datetime, timedelta

# --- Базовая структура MiniCRM (Этап 1) ---

# Конфигурация и демо-данные
DEMO_DATA = {
    "contacts": [
        {"id": 1, "name": "Иван Иванов", "phone": "+79001234567", "email": "ivan@example.com"},
        {"id": 2, "name": "Мария Петрова", "phone": "+79007654321", "email": "maria@example.com"}
    ],
    "deals": [
        {"id": 1, "contact_id": 1, "title": "Покупка CRM", "amount": 50000, "stage": "Новая", "date": datetime.now().strftime("%Y-%m-%d")}
    ],
    "reminders": [
        {"id": 1, "text": "Позвонить Ивану Иванову", "due_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M")}
    ]
}

# Простая консольная точка входа для демонстрации
def run_demo():
    print("=== MiniCRM Demo ===")
    print(f"Контактов: {len(DEMO_DATA['contacts'])}")
    print(f"Сделок: {len(DEMO_DATA['deals'])}")
    print(f"Напоминаний: {len(DEMO_DATA['reminders'])}")
    
    # Пример вывода списка контактов
    for contact in DEMO_DATA["contacts"]:
        print(f"- {contact['name']}: {contact['phone']}")

if __name__ == "__main__":
    run_demo()
