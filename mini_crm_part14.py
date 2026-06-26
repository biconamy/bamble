# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MiniCRM
def generate_summary():
    summary = []
    if contacts:
        contact_count = len(contacts)
        active_contacts = sum(1 for c in contacts if c.get('is_active', True))
        summary.append(f"Контактов: {contact_count} (активных: {active_contacts})")
    
    if deals:
        deal_count = len(deals)
        open_deals = sum(1 for d in deals if d.get('status') != 'closed')
        total_value = sum(d.get('value', 0) for d in deals)
        summary.append(f"Сделок: {deal_count} (открытых: {open_deals}, сумма: {total_value})")
    
    if reminders:
        today = datetime.now().date()
        upcoming_reminders = [r for r in reminders if r.get('due_date', '').date() >= today]
        summary.append(f"Напоминаний сегодня/впереди: {len(upcoming_reminders)}")
    
    if messages:
        unread_count = sum(1 for m in messages if not m.get('is_read', False))
        summary.append(f"Сообщений (непрочитанных): {unread_count}")
    
    print("=== СВОДКА MiniCRM ===")
    for line in summary:
        print(line)
