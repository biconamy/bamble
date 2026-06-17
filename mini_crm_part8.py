# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MiniCRM
def show_menu():
    print("\n=== MiniCRM Меню ===")
    print("1. Добавить контакт")
    print("2. Просмотреть контакты")
    print("3. Добавить сделку")
    print("4. Просмотреть сделки")
    print("5. Напоминания")
    print("6. История общения")
    print("0. Выход")

def handle_choice(choice):
    if choice == "1":
        name = input("Имя: ")
        phone = input("Телефон: ")
        contacts.append({"name": name, "phone": phone})
        print(f"Контакт {name} добавлен.")
    elif choice == "2":
        for c in contacts:
            print(f"{c['name']} - {c['phone']}")
    elif choice == "3":
        contact_name = input("Имя контакта: ")
        deal_value = float(input("Стоимость сделки: "))
        deals.append({"contact": contact_name, "value": deal_value})
        print(f"Сделка добавлена.")
    elif choice == "4":
        for d in deals:
            print(f"{d['contact']} - {d['value']:.2f}")
    elif choice == "5":
        if reminders:
            for r in reminders:
                print(r)
        else:
            print("Напоминаний нет.")
    elif choice == "6":
        contact_name = input("Имя контакта: ")
        history = [h for h in history_log if h.get('contact') == contact_name]
        if history:
            for h in history:
                print(f"{h['date']}: {h['message']}")
        else:
            print("Нет истории для этого контакта.")
    elif choice == "0":
        print("Выход из программы.")
