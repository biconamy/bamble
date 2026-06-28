# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MiniCRM
def get_monthly_stats(start_date, end_date):
    stats = {'contacts': 0, 'deals': 0, 'messages': 0}
    for contact in contacts:
        if start_date <= contact['created_at'] <= end_date:
            stats['contacts'] += 1
    for deal in deals:
        if start_date <= deal['created_at'] <= end_date:
            stats['deals'] += 1
    for msg in messages:
        if start_date <= msg['timestamp'] <= end_date:
            stats['messages'] += 1
    return stats

def get_monthly_stats(start_date, end_date):
    from datetime import date
    year = start_date.year
    month = start_date.month
    stats = {'contacts': 0, 'deals': 0, 'messages': 0}
    
    for contact in contacts:
        if contact['created_at'].year == year and contact['created_at'].month == month:
            stats['contacts'] += 1
            
    for deal in deals:
        if deal['created_at'].year == year and deal['created_at'].month == month:
            stats['deals'] += 1
            
    for msg in messages:
        if msg['timestamp'].year == year and msg['timestamp'].month == month:
            stats['messages'] += 1
            
    return stats
