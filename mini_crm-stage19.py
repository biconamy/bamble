# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MiniCRM
def archive_records(archive_age_days=365):
    today = datetime.date.today()
    for record_type in ['contacts', 'deals', 'notes']:
        records_to_archive = []
        for key, value in db[record_type].items():
            if isinstance(value.get('created_at'), str):
                created_date = datetime.strptime(value['created_at'], '%Y-%m-%d')
            else:
                continue
            age_days = (today - created_date).days
            status = value.get('status', 'active')
            is_old = age_days > archive_age_days or (record_type == 'deals' and status in ['closed', 'lost'])
            if is_old:
                records_to_archive.append(key)
        for key in records_to_archive:
            db[record_type][key]['archived'] = True
            print(f"Archived {record_type}: {db[record_type][key].get('name') or db[record_type][key].get('title')}")
