from playwright.sync_api import Page

from pages.base_model import Base_page


class Expenses_model(Base_page):
    def __init__(self, page: Page):
        super().__init__(page)

        self.path = '/panel/expenses'

    def go_to(self, item_id: str = None):
        if item_id:
            self.navigate(self.path + '/' + item_id)
        else: self.navigate(self.path) # base_url + self.path