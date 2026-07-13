# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MiniCRM
def print_contact(contact):
    """Компактный вывод одной записи контакта с деталями."""
    if not contact:
        return "Нет контактов."
    lines = [f"Имя: {contact.get('name', 'Не указано')}", f"Email: {contact.get('email', 'Не указан')}"]
    phone = contact.get('phone', '')
    if phone:
        lines.append(f"Телефон: {phone}")
    company = contact.get('company', 'Без компании')
    if company != "Без компании":
        lines.append(f"Компания: {company}")
    tags = contact.get('tags', [])
    if tags:
        lines.append(f"Теги: {', '.join(tags)}")
    notes = contact.get('notes', '')
    if notes:
        lines.append(f"Заметки: {notes}")
    print("\n".join(lines))
