# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MiniCRM
def get_metrics():
    metrics = {}
    contacts = db.contacts.values()
    deals = db.deals.values()
    reminders = db.reminders.values()
    communications = db.communications.values()

    total_contacts = len(contacts)
    active_deals = sum(1 for d in deals if d['status'] == 'active')
    closed_deals = sum(1 for d in deals if d['status'] in ('closed', 'lost'))
    pending_reminders = sum(1 for r in reminders if r['date'] > datetime.date.today())

    avg_comm_count_per_contact = (len(communications) / total_contacts) if total_contacts else 0
    active_deals_ratio = (active_deals / len(deals)) if deals else 0

    metrics['contacts_total'] = total_contacts
    metrics['deals_active'] = active_deals
    metrics['deals_closed'] = closed_deals
    metrics['deals_pending_reminders'] = pending_reminders
    metrics['avg_communications_per_contact'] = round(avg_comm_count_per_contact, 2)
    metrics['active_deals_ratio'] = round(active_deals_ratio * 100, 2)

    return metrics
