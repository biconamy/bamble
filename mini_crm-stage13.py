# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MiniCRM
def search_contacts(query: str) -> list[dict]:
    if not query.strip(): return []
    q = query.lower()
    results = []
    for contact in contacts:
        fields_to_check = [contact.get('name', '').lower(), contact.get('phone', '').lower()]
        if any(q in f for f in fields_to_check):
            results.append(contact)
    return results
