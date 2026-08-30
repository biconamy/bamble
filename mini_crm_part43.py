# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MiniCRM
class Pager:
    def __init__(self, data, page_size=20):
        self.data = list(data)
        self.page_size = page_size
        self.current_page = 1

    def page(self):
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return {
            'page': self.current_page,
            'total_pages': (len(self.data) + self.page_size - 1) // self.page_size if self.data else 0,
            'items': self.data[start:end],
            'has_next': end < len(self.data),
            'has_prev': self.current_page > 1,
        }

    def next_page(self):
        if self.current_page < self.total_pages() or not self.data:
            self.current_page += 1
        return self.page()

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self.page()

    def total_pages(self):
        return (len(self.data) + self.page_size - 1) // self.page_size if self.data else 0
