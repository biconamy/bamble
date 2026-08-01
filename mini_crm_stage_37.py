# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MiniCRM
import unittest


class TestMiniCRM(unittest.TestCase):
    def test_add_contact(self):
        crm = MiniCRM()
        crm.add_contact("Иван", "+79001234567")
        self.assertEqual(len(crm.contacts), 1)
        self.assertEqual(crm.contacts[0]["name"], "Иван")

    def test_add_deal(self):
        crm = MiniCRM()
        crm.add_contact("Петр", "+79007654321")
        crm.add_deal("Петр", 500, "Покупка товара")
        self.assertEqual(len(crm.deals), 1)

    def test_add_reminder(self):
        crm = MiniCRM()
        crm.add_contact("Анна", "+79001112233")
        crm.add_reminder("Анна", "Позвонить", "2025-12-01")
        self.assertEqual(len(crm.reminders), 1)

    def test_add_message(self):
        crm = MiniCRM()
        crm.add_contact("Сергей", "+79004445566")
        crm.add_message("Сергей", "Привет! Как дела?", "2025-12-10")
        self.assertEqual(len(crm.messages), 1)

    def test_add_to_watchlist(self):
        crm = MiniCRM()
        crm.add_contact("Виктор", "+79008889900")
        crm.add_to_watchlist("Виктор", "Заинтересован в курсе")
        self.assertEqual(len(crm.watchlist), 1)

    def test_add_event(self):
        crm = MiniCRM()
        crm.add_contact("Ольга", "+79003334455")
        crm.add_event("Ольга", "День рождения", "2026-01-15")
        self.assertEqual(len(crm.events), 1)

    def test_add_note(self):
        crm = MiniCRM()
        crm.add_contact("Дмитрий", "+79002223344")
        crm.add_note("Дмитрий", "Любит кофе по пятницам")
        self.assertEqual(len(crm.notes), 1)

    def test_add_to_blacklist(self):
        crm = MiniCRM()
        crm.add_contact("Елена", "+79006667788")
        crm.add_to_blacklist("Елена", "Спам")
        self.assertEqual(len(crm.blacklist), 1)

    def test_add_task(self):
        crm = MiniCRM()
        crm.add_contact("Мария", "+79005556677")
        crm.add_task("Мария", "Отправить отчет", "2025-12-30")
        self.assertEqual(len(crm.tasks), 1)

    def test_add_to_team(self):
        crm = MiniCRM()
        crm.add_contact("Алексей", "+79004445566")
        crm.add_to_team("Алексей", "Менеджер по продажам")
        self.assertEqual(len(crm.teams), 1)


if __name__ == "__main__":
    unittest.main()
