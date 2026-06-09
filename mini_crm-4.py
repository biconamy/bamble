# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MiniCRM
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in record_fields and key in records[record_id]:
            records[record_id][key] = value
        else:
            print(f"Поле '{key}' не существует или недоступно для редактирования.")
            return False
    
    print(f"Запись с ID {record_id} успешно обновлена.")
    return True

# Пример вызова (раскомментируй при тестировании):
# edit_record(1, {"name": "Иванов И.И.", "phone": "+79001234567"})
