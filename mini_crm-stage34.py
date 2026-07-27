# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MiniCRM
class Template:
    def __init__(self, name, fields=None):
        self.name = name
        self.fields = fields or []  # list of (field_name, default_value) tuples

    def create_record(self, **kwargs):
        record = {}
        for fname, fdefault in self.fields:
            if fname in kwargs:
                record[fname] = kwargs.pop(fname)
            else:
                record[fname] = fdefault
        return record


def add_templates_to_db(db):
    templates_table = db["templates"]  # {name: Template}
    for tmpl_name, fields in [
        ("contact_quick", [("last_name", ""), ("phone", "")]),
        ("deal_init", [("title", ""), ("client_last_name", ""), ("amount", 0), ("deadline", None)]),
        ("followup_reminder", [("subject", "Follow-up"), ("message_template", "Hello, just checking in."), ("date", datetime.now())]),
    ]:
        if tmpl_name not in templates_table:
            templates_table[tmpl_name] = Template(tmpl_name, fields)
