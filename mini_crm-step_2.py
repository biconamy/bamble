# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MiniCRM
class ValidationError(Exception):
    pass

def validate_email(email: str) -> bool:
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValidationError("Некорректный формат email")
    return True

def validate_phone(phone: str) -> bool:
    phone = phone.replace(' ', '').replace('-', '')
    if not phone.isdigit() or len(phone) < 10:
        raise ValidationError("Некорректный номер телефона")
    return True

def validate_date(date_str: str) -> bool:
    try:
        year, month, day = map(int, date_str.split('.'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValidationError("Некорректные день или месяц")
        return True
    except ValueError:
        raise ValidationError("Некорректный формат даты (ДД.ММ.ГГГГ)")

def validate_amount(amount: str) -> bool:
    try:
        val = float(amount)
        if val < 0:
            raise ValidationError("Сумма сделки не может быть отрицательной")
        return True
    except ValueError:
        raise ValidationError("Некорректная сумма")
