# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: MiniCRM
def get_next_actions(self) -> dict:
    """Generate next-action recommendations based on current state."""
    actions = []
    
    # Check overdue follow-ups from reminders
    now = datetime.now()
    for reminder in self.reminders:
        if (now - timedelta(days=1)) <= (now - reminder["date"]) and reminder.get("done") is False:
            contact_name = self.contacts[reminder["contact_id"]]["name"] if reminder["contact_id"] in self.contacts else "Unknown"
            actions.append({
                "type": "follow_up",
                "priority": 1,
                "message": f"Follow up with {contact_name} - overdue by {(now - reminder['date']).days} days"
            })

    # Check deals that are older than expected duration without update
    for deal in self.deals:
        if (now - timedelta(days=3)) <= (now - deal["date"]) and deal.get("updated") is False:
            actions.append({
                "type": "deal_update",
                "priority": 2,
                "message": f"Update progress for deal with {deal['name']} - no updates in last 3 days"
            })

    # Check contacts without recent communication (last 14 days)
    for contact_id, contact in self.contacts.items():
        if contact.get("last_communication_date"):
            if (now - timedelta(days=14)) <= (now - contact["last_communication_date"]) and contact.get("updated") is False:
                actions.append({
                    "type": "re_engage",
                    "priority": 3,
                    "message": f"Re-engage with {contact['name']} - no communication in last 14 days"
                })

    # Sort by priority
    actions.sort(key=lambda x: x["priority"])
    return {"actions": actions}
