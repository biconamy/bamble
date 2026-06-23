# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MiniCRM
import json, os

def load_from_file(filepath: str) -> dict:
    try:
        if not os.path.exists(filepath):
            print(f"Файл {filepath} не найден.")
            return {}
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                for key in ['contacts', 'deals', 'reminders']:
                    if key not in data:
                        data[key] = []
                print("Данные успешно загружены из JSON.")
                return data
            else:
                raise ValueError("Неверный формат данных в файле (ожидался словарь).")
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON файла {filepath}: некорректный синтаксис. Детали: {e}")
        return {}
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {type(e).__name__}.")
        return {}
