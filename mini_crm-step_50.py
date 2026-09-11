# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: MiniCRM
def _format_message(sender: str, content: str, timestamp: datetime) -> str:
    """Оформляет строку сообщения в истории общения."""
    return f"[{timestamp.strftime('%H:%M')} | {sender}] {content}"

def _format_contact(contact: dict) -> str:
    """Контактная карточка для отчёта."""
    return (f"Имя: {contact['name']}, "
            f"Телефон: {contact.get('phone', 'N/A')}, "
            f"Email: {contact.get('email', 'N/A')}, "
            f"Компания: {contact.get('company', 'N/A')}")

def _format_deal(deal: dict) -> str:
    """Карточка сделки для отчёта."""
    return (f"Название: {deal['name']}, "
            f"Клиент: {deal.get('client_name', 'N/A')}, "
            f"Статус: {deal['status']}, "
            f"Сумма: {deal.get('amount', 0):,.2f} руб.")

def _format_reminder(reminder: dict) -> str:
    """Напоминание для отчёта."""
    return (f"Заголовок: {reminder['title']}, "
            f"Дата: {reminder['date']}, "
            f"Время: {reminder['time']}, "
            f"Описание: {reminder.get('description', '')}")

def _format_history(history: list) -> str:
    """История общения в виде отчёта."""
    lines = []
    for msg in history:
        lines.append(_format_message(msg['sender'], msg['content'], msg['timestamp']))
    return "\n".join(lines)

def _save_all() -> None:
    """Сохраняет все данные в JSON-файлы."""
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    with open("deals.json", "w", encoding="utf-8") as f:
        json.dump(deals, f, ensure_ascii=False, indent=2)
    with open("reminders.json", "w", encoding="utf-8") as f:
        json.dump(reminders, f, ensure_ascii=False, indent=2)
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def _load_all() -> None:
    """Загружает данные из JSON-файлов."""
    global contacts, deals, reminders, history
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    try:
        with open("deals.json", "r", encoding="utf-8") as f:
            deals = json.load(f)
    except FileNotFoundError:
        deals = []
    try:
        with open("reminders.json", "r", encoding="utf-8") as f:
            reminders = json.load(f)
    except FileNotFoundError:
        reminders = []
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

def _generate_id(prefix: str) -> str:
    """Генерирует уникальный ID для записи."""
    return f"{prefix}_{int(time.time() * 1000)}"

def _validate_contact(contact: dict) -> bool:
    """Проверяет корректность контактных данных."""
    if not contact.get("name"):
        return False
    if not contact.get("phone") and not contact.get("email"):
        return False
    return True

def _validate_deal(deal: dict) -> bool:
    """Проверяет корректность данных сделки."""
    if not deal.get("name"):
        return False
    if not deal.get("client_name"):
        return False
    if deal.get("amount", 0) < 0:
        return False
    return True

def _validate_reminder(reminder: dict) -> bool:
    """Проверяет корректность данных напоминания."""
    if not reminder.get("title"):
        return False
    return True
