# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MiniCRM
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_keys = ['contacts', 'deals', 'reminders']
        for key in required_keys:
            if not isinstance(data.get(key), list):
                raise ValueError(f"Отсутствует или неверно типизирован ключ '{key}'")
        
        # Преобразование типов для обеспечения совместимости с остальным кодом проекта
        processed_data = {
            'contacts': data['contacts'],
            'deals': data['deals'],
            'reminders': data['reminders'],
            'history': data.get('history', [])
        }
        
        return processed_data
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Отсутствует обязательное поле в данных: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для теста с реальным JSON):
if __name__ == "__main__":
    # json_string = '{"contacts":[...], "deals":[...], ...}'  # Замените на вашу строку
    initial_data = load_initial_data(json_string)
