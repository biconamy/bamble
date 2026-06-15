# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MiniCRM
def sort_records(records, field='date', reverse=False):
    if field == 'date':
        return sorted(records, key=lambda r: r.get('created_at') or 0, reverse=reverse)
    elif field == 'priority':
        priority_map = {'high': 1, 'medium': 2, 'low': 3}
        return sorted(records, key=lambda r: priority_map.get(r.get('priority', 'medium'), 2), reverse=True)
    else: # name
        return sorted(records, key=lambda r: (r.get('name') or '').lower(), reverse=False)
