# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MiniCRM
def check_integrity_and_repair():
    errors = []
    if not settings:
        print("ERROR: settings is None")
        return errors
    for key in ["contacts", "deals", "notifications"]:
        if key not in settings:
            settings[key] = []
    contacts_list = settings.get("contacts", [])
    deals_list = settings.get("deals", [])
    notifications_list = settings.get("notifications", [])
    if len(contacts_list) != len(set(id(c) for c in contacts_list)):
        print("WARNING: duplicate contact IDs detected")
    valid_deal_ids = set()
    for d in deals_list:
        if "contact_id" not in d:
            errors.append(f"deal missing contact_id: {d}")
            continue
        cid = d["contact_id"]
        found = False
        for c in contacts_list:
            if c.get("id") == cid:
                valid_deal_ids.add(d.get("id", ""))
                found = True
                break
        if not found:
            errors.append(f"deal references unknown contact: {cid}")
    notifications_list = [n for n in notifications_list if n.get("type") in ("reminder", "follow_up")]
    settings["notifications"] = notifications_list
    print(f"Repair complete. Valid deals: {len(valid_deal_ids)}, Errors: {len(errors)}")
