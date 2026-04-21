from playwright.sync_api import Page

from pages.base_model import Base_page


class Profile_model(Base_page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = '/panel/profile'
        self.profile_settings_link = page.get_by_text("Profile Settings")
        self.profile_nav_link = page.get_by_role("link", name=" Profile")
        self.user_name_text = page.get_by_text("Sasha Nedz")
        self.edit_profile_button = page.get_by_role("button", name="Edit profile")
        self.edit_profile_form = page.locator("form")
        self.input_name = page.get_by_role("textbox", name="Name", exact=True)

    def go_to(self):
        self.navigate(self.path)

    def open_via_sidebar(self):
        self.profile_settings_link.click()
        self.profile_nav_link.click()

    def click_edit_profile(self):
        self.edit_profile_button.click()

    def verify_edit_form_fields(self):
        expect(self.edit_profile_form).to_contain_text("Name")
        expect(self.edit_profile_form).to_contain_text("Last name")
        expect(self.edit_profile_form).to_contain_text("Country")
        expect(self.edit_profile_form).to_contain_text("Birthday")
