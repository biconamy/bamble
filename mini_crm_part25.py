# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MiniCRM
def parse_date(date_str):
    """Парсит дату из строки в datetime.date, возвращая None при ошибке."""
    if not date_str or not isinstance(date_str, str):
        return None
    formats = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%Y%m%d"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

def format_date(dt):
    """Форматирует datetime.date в строку YYYY-MM-DD."""
    if dt is None or not isinstance(dt, datetime.date):
        return ""
    return dt.strftime("%Y-%m-%d")

def validate_contact(contact):
    """Валидирует контакт: имя, телефон, email. Возвращает список ошибок."""
    errors = []
    if not contact.get("name") or not isinstance(contact["name"], str) or not contact["name"].strip():
        errors.append("Имя обязательно.")
    phone = contact.get("phone", "")
    if phone and (not str(phone).replace("-", "").replace("+7", "").replace(" ", "").isdigit() or len(str(phone).replace("-", "").replace("+7", "").replace(" ", "")) < 10):
        errors.append("Неверный формат телефона.")
    email = contact.get("email", "")
    if email and "@" not in str(email) or "." not in str(email):
        errors.append("Некорректный email.")
    return errors

def validate_deal(deal):
    """Валидирует сделку: сумма, статус, даты."""
    errors = []
    amount = deal.get("amount")
    if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
        errors.append("Сумма должна быть положительным числом.")
    status = deal.get("status", "new")
    if status not in ("new", "in_progress", "closed"):
        errors.append(f"Неизвестный статус: {status}. Допустимы: new, in_progress, closed.")

    close_date = parse_date(deal.get("close_date"))
    start_date = parse_date(deal.get("start_date"))
    if close_date and not (start_date <= close_date):
        errors.append("Дата начала сделки не может быть после даты закрытия.")

    return errors
