# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MiniCRM
def delete_record(table_name, record_id):
    if not table_name or not isinstance(record_id, int) or record_id <= 0:
        raise ValueError("Некорректные параметры для удаления.")
    
    db[table_name].pop(record_id - 1, None)
