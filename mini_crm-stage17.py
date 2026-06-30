# === Stage 17: Добавь группировку записей по категориям ===
# Project: MiniCRM
class CategoryManager:
    def __init__(self, db):
        self.db = db
    
    def add_category(self, name):
        if not any(c['name'] == name for c in self.db.categories):
            self.db.categories.append({'id': len(self.db.categories) + 1, 'name': name})
    
    def get_categories(self):
        return sorted(self.db.categories, key=lambda x: x['name'])
    
    def filter_records_by_category(self, records, category_name):
        if not any(c['name'] == category_name for c in self.db.categories):
            return []
        cat_id = next((c['id'] for c in self.db.categories if c['name'] == category_name), None)
        return [r for r in records if r.get('category') and str(r['category']) == str(cat_id)]
