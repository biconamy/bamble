# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MiniCRM
# ── MiniCRM v0.15 — миграция структуры данных ──

def migrate_contacts():
    """
    Переход v0.14 -> v0.15:
    - добавляем колонку 'notes' (текстовая заметка к контакту)
    - добавляем колонку 'last_interaction' (дата последнего контакта)
    """
    global contacts

    new_contacts = []
    for c in contacts:
        new_contact = {
            "id": c["id"],
            "name": c["name"],
            "email": c["email"],
            "phone": c["phone"],
            "company": c.get("company", ""),
            "status": c.get("status", "active"),
            "notes": c.get("notes", ""),
            "last_interaction": c.get("last_interaction", None),
        }
        new_contacts.append(new_contact)

    contacts = new_contacts

    print("Migration completed: contacts now include 'notes' and 'last_interaction'.")
