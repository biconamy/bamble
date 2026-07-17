# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MiniCRM
def reset_demo_data():
    """Сбросить демо-данные в контакты, сделки и напоминания."""
    import os, sys
    
    demo_contacts = [
        {"id": 1, "name": "Иван Иванов", "phone": "+7 (900) 123-45-67", "email": "ivan@example.com"},
        {"id": 2, "name": "Мария Петрова", "phone": "+7 (900) 765-43-21", "email": "maria@example.com"}
    ]
    demo_deals = [
        {"id": 1, "contact_id": 1, "title": "Купить CRM", "amount": 50000, "status": "new"},
        {"id": 2, "contact_id": 2, "title": "Партнёрство", "amount": 100000, "status": "in_progress"}
    ]
    demo_reminders = [
        {"id": 1, "text": "Напомнить про встречу с Иваном", "date": datetime(2024, 3, 25).strftime("%Y-%m-%d")}
    ]
    
    contacts_data.save(demo_contacts)
    deals_data.save(demo_deals)
    reminders_data.save(demo_reminders)
