# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: MiniCRM
APP_CONFIG = {
    "app_name": "MiniCRM",
    "version": 29,
    "description": "Simple CRM for contacts, deals, reminders and history",
    "default_language": "ru",
    "max_contacts_per_page": 10,
    "max_deals_per_page": 10,
    "history_limit": 5,
}


def get_config():
    """Возвращает текущую конфигурацию приложения."""
    return APP_CONFIG.copy()


def set_config(key, value):
    """Устанавливает или обновляет значение в конфигурации."""
    if key not in APP_CONFIG:
        raise ValueError(f"Unknown config key: {key}")
    APP_CONFIG[key] = value


def print_config():
    """Выводит текущую конфигурацию приложения."""
    for k, v in sorted(APP_CONFIG.items()):
        print(f"{k}: {v}")


# Пример использования:
if __name__ == "__main__":
    print("=== Конфигурация MiniCRM ===")
    print_config()

    # Изменение конфигурации
    set_config("history_limit", 3)
    set_config("max_contacts_per_page", 20)
    print("\nОбновлённая конфигурация:")
    print_config()
