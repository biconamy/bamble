# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MiniCRM
def self_check():
    print("=== MiniCRM Self-Check ===")
    try:
        app = MiniCRM()
        app.create_contact("Иван Иванов", "+79001112233", "ivan@example.com", "Москва", "Бизнес")
        app.create_contact("Петр Петров", "+79004445566", "petr@example.com", "СПб", "Частный")
        app.create_deal("Сделка-1", "Продукт А", "Иван Иванов", 50000, "Активная")
        app.create_deal("Сделка-2", "Продукт Б", "Петр Петров", 75000, "В работе")
        app.create_reminder("Позвонить Ивану", "2024-12-31", "10:00", "Иван Иванов")
        app.create_reminder("Напоминание Петру", "2024-12-30", "15:00", "Петр Петров")
        app.add_log("Иван Иванов", "Первое общение", "Обсудить сотрудничество", "2024-12-01")
        app.add_log("Петр Петров", "Первое общение", "Предложить встречу", "2024-12-02")
        app.add_log("Иван Иванов", "Следующее общение", "Обсудить детали", "2024-12-03")
        app.add_log("Петр Петров", "Следующее общение", "Отправить документ", "2024-12-04")
        app.add_log("Иван Иванов", "Завершение", "Подписан договор", "2024-12-05")
        assert app.get_contacts() == 2
        assert app.get_deals() == 2
        assert app.get_reminders() == 2
        assert app.get_logs() == 5
        print("✓ Все тесты пройдены успешно!")
        print(f"✓ Контакты: {app.get_contacts()}")
        print(f"✓ Сделки: {app.get_deals()}")
        print(f"✓ Напоминания: {app.get_reminders()}")
        print(f"✓ История: {app.get_logs()}")
    except Exception as e:
        print(f"✗ Ошибка: {e}")
