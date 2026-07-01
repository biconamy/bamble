# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MiniCRM
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, name):
        if not any(t['name'] == name for t in self.db.tags):
            self.db.tags.append({'id': len(self.db.tags) + 1, 'name': name})
    
    def remove_tag(self, tag_id):
        self.db.tags = [t for t in self.db.tags if t['id'] != tag_id]
    
    def add_contact_tags(self, contact_id, tags):
        for tag_name in tags:
            existing = next((t for t in self.db.tags if t['name'] == tag_name), None)
            if not existing:
                self.add_tag(tag_name)
                existing = next(t for t in self.db.tags if t['name'] == tag_name)
        contact_tags = [t for c in self.db.contacts if c['id'] == contact_id]
        if contact_tags:
            contact_tags[0]['tags'] = list(set(contact_tags[0].get('tags', []) + tags))
    
    def remove_contact_tags(self, contact_id, tags):
        contact_tags = [t for c in self.db.contacts if c['id'] == contact_id]
        if contact_tags:
            current_tags = set(contact_tags[0].get('tags', []))
            to_remove = {tag_name for tag_name in tags if any(t['name'] == tag_name for t in self.db.tags)}
            current_tags -= to_remove
            contact_tags[0]['tags'] = list(current_tags)
