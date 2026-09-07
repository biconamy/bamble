# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: MiniCRM
def _format_history_entry(entry):
    """Compact representation of a single history entry."""
    return f"[{entry['date']} {entry['time']}] {entry.get('user', 'System')}: {entry.get('message', '')}"

def _format_contact_history(contact_id, history):
    """Format full history of a contact."""
    if not history:
        return "История пуста."
    lines = [_format_history_entry(h) for h in history]
    return "\n".join(lines)

def _format_lead_history(lead_id, history):
    """Format full history of a lead."""
    if not history:
        return "История пуста."
    lines = [_format_history_entry(h) for h in history]
    return "\n".join(lines)
