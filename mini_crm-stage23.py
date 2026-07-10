# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MiniCRM
def print_table(headers, rows):
    """Формирует и выводит таблицу в консоль."""
    if not headers:
        return
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            w = len(str(val))
            if i < len(widths):
                widths[i] = max(widths[i], w)

    fmt = " | ".join(f"{{:<{w}}}" for w in widths) + " |"
    lines = [fmt.format(*headers)]
    sep = "-+-".join("-" * w for w in widths)
    lines.append(sep)
    for row in rows:
        lines.append(fmt.format(*row))

    print("\n".join(lines))


def console_demo():
    """Демонстрация работы MiniCRM через таблицу в консоли."""
    contacts = [
        {"id": 1, "name": "Алексей", "company": "ООО Ромашка"},
        {"id": 2, "name": "Мария", "company": "ЗАО Вишня"},
        {"id": 3, "name": "Дмитрий", "company": null},
    ]

    print_table(
        ["ID", "Имя", "Компания"],
        [c["id"] for c in contacts],
        [c["name"] for c in contacts],
        [c.get("company") or "-" for c in contacts],
    )


console_demo()
