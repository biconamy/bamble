# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MiniCRM
def undo_last_action():
    """Откат последнего действия CRM: удаляет последнюю запись из истории действий."""
    if not actions_history:
        print("История действий пуста, откатить нечего.")
        return None
    
    last_action = actions_history.pop()
    print(f"Откаты действие: {last_action}")
    return last_action

# Пример использования
try:
    undo_last_action()
except Exception as e:
    print(f"Ошибка при откате: {e}")
