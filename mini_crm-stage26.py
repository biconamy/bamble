# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MiniCRM
import random

def demo_commands():
    """Генератор демо-команд для ручного тестирования MiniCRM."""
    contacts = [
        {"id": "d1", "name": "Иван Петров", "phone": "+79001234567", "email": "ivan@example.com", "company": "ООО Ромашка"},
        {"id": "d2", "name": "Мария Сидорова", "phone": "+79007654321", "email": "maria@example.com", "company": "ЗАО Вишня"},
        {"id": "d3", "name": "Алексей Козлов", "phone": "+79001112233", "email": "alexey@example.com", "company": ""},
    ]
    deals = [
        {"id": "de1", "contact_id": "d1", "name": "Купля CRM", "amount": 15000, "stage": "В работе"},
        {"id": "de2", "contact_id": "d3", "name": "Сервисное соглашение", "amount": 5000, "stage": "Закрыта"},
    ]
    reminders = [
        {"id": "r1", "text": "Позвонить Ивану о продлении договора", "date": "2026-08-10"},
        {"id": "r2", "text": "Отправить Мариям коммерческое предложение", "date": "2026-08-15"},
    ]
    messages = [
        {"id": "m1", "contact_id": "d1", "text": "Здравствуйте, интересна CRM?", "role": "client"},
        {"id": "m2", "contact_id": "d1", "text": "Давайте обсудим детали.", "role": "user"},
    ]

    demo = []
    demo.append({"action": "add_contact", "payload": contacts[0].copy()})
    demo.append({"action": "list_contacts"})
    demo.append({"action": "show_deals", "contact_id": "d1"})
    demo.append({"action": "add_reminder", "payload": {"text": "Напомнить Ивана о встрече", "date": "2026-08-05"}})
    demo.append({"action": "list_messages", "filter": {"contact_id": "d1"}})

    for i in range(3):
        demo.append({"action": "random_demo", "payload": {}})

    return demo
