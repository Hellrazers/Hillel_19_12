from playwright.sync_api import Page, expect

from pages.profile_model import Profile_model


def test_profile_edit_form_fields_visible(ui_login_multy):
    page: Page = ui_login_multy()
    profile_page = Profile_model(page)

    profile_page.open_via_sidebar()
    profile_page.click_edit_profile()
    profile_page.verify_edit_form_fields()

    profile_page.input_name.click()


def test_profile_user_name_visible(ui_login_multy):
    page: Page = ui_login_multy()
    profile_page = Profile_model(page)

    profile_page.open_via_sidebar()

    expect(profile_page.user_name_text).to_be_visible()
