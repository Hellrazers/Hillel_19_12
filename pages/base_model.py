from playwright.sync_api import Page, expect


class Base_page:
    def __init__(self, page: Page):
        self.page:Page = page
        self.notify_element = page.locator('//div[@class="alert alert-success"]/p')


        #modal
        self.modal_title = page.locator('//*[@class="modal-title"]')
        self.modal_add_button = page.get_by_role('button', name='Add')


    def navigate(self, path: str):
        self.page.goto(path)

    def notify_verify_text(self, expected_text: str):

        expect(self.notify_element).to_have_text(expected_text)


