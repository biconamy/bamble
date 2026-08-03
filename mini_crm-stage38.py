# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MiniCRM
import unittest

class TestEdgeCases(unittest.TestCase):
    def test_add_contact_duplicate_name(self):
        crm = MiniCRM()
        crm.add_contact("Иван Иванов", "+79001234567")
        with self.assertRaises(ValueError):
            crm.add_contact("Иван Иванов", "+79007654321")

    def test_add_deal_no_amount(self):
        crm = MiniCRM()
        crm.add_contact("Петр Петров", "+79001112233")
        with self.assertRaises(ValueError):
            crm.add_deal("PET-001", "Дорогой товар", 0, "Иван Иванов", 5)

    def test_add_reminder_no_date(self):
        crm = MiniCRM()
        crm.add_contact("Сидор Сидоров", "+79004445566")
        with self.assertRaises(ValueError):
            crm.add_reminder("Найти Сидора", "Иван Иванов", None)

    def test_add_message_no_sender(self):
        crm = MiniCRM()
        crm.add_contact("Нина Никитична", "+79007778899")
        with self.assertRaises(ValueError):
            crm.add_message(None, "Привет")

    def test_add_history_no_date(self):
        crm = MiniCRM()
        crm.add_contact("Олег Олегович", "+79003334455")
        with self.assertRaises(ValueError):
            crm.add_history("Обсуждение условий", "Иван Иванов", None)

    def test_add_note_no_title(self):
        crm = MiniCRM()
        crm.add_contact("Валерий Валентинович", "+79006667788")
        with self.assertRaises(ValueError):
            crm.add_note("", "Срочно перезвонить")

    def test_get_deals_empty(self):
        crm = MiniCRM()
        self.assertEqual(len(crm.get_deals()), 0)

    def test_search_contacts_no_results(self):
        crm = MiniCRM()
        crm.add_contact("Анна Андреевна", "+79001234567")
        results = crm.search_contacts("не существует")
        self.assertEqual(len(results), 0)

    def test_search_history_no_results(self):
        crm = MiniCRM()
        crm.add_contact("Борис Борисович", "+79002223344")
        results = crm.search_history("не найдено")
        self.assertEqual(len(results), 0)

    def test_search_messages_no_results(self):
        crm = MiniCRM()
        crm.add_contact("Виктория Викторовна", "+79005556677")
        results = crm.search_messages("нет таких сообщений")
        self.assertEqual(len(results), 0)

    def test_search_notes_no_results(self):
        crm = MiniCRM()
        crm.add_contact("Дмитрий Дмитриевич", "+79008889900")
        results = crm.search_notes("ничего не найдено")
        self.assertEqual(len(results), 0)

    def test_search_reminders_no_results(self):
        crm = MiniCRM()
        crm.add_contact("Елена Евгеньевна", "+79001123456")
        results = crm.search_reminders("не существует")
        self.assertEqual(len(results), 0)

    def test_search_deals_no_results(self):
        crm = MiniCRM()
        crm.add_contact("Жан Жанович", "+79004456789")
        results = crm.search_deals("нет таких сделок")
        self.assertEqual(len(results), 0)

    def test_add_note_empty_text(self):
        crm = MiniCRM()
        crm.add_contact("Зоя Зиновьевна", "+79006543210")
        with self.assertRaises(ValueError):
            crm.add_note("Тестовая заметка", "")

    def test_add_reminder_empty_text(self):
        crm = MiniCRM()
        crm.add_contact("Алексей Алексеевич", "+79007654321")
        with self.assertRaises(ValueError):
            crm.add_reminder("", "Иван Иванов", datetime.date(2024, 1, 25))

    def test_add_message_empty_text(self):
        crm = MiniCRM()
        crm.add_contact("Майя Михайловна", "+79008765432")
        with self.assertRaises(ValueError):
            crm.add_message("Иван Иванов", "")

    def test_get_deals_empty_amount(self):
        crm = MiniCRM()
        crm.add_contact("Наталья Николаевна", "+79009876543")
        deal_id = "PET-TEST"
        with self.assertRaises(ValueError):
            crm.get_deals(deal_id, 0)

    def test_get_deals_no_date(self):
        crm = MiniCRM()
        crm.add_contact("Ольга Осиповна", "+79001234567")
        deal_id = "PET-TEST"
        with self.assertRaises(ValueError):
            crm.get_deals(deal_id, 100, date=None)

    def test_get_deals_no_amount_or_date(self):
        crm = MiniCRM()
        crm.add_contact("Павел Павлович", "+79002345678")
        deal_id = "PET-TEST"
        with self.assertRaises(ValueError):
            crm.get_deals(deal_id, 0, date=None)

if __name__ == '__main__':
    unittest.main()
