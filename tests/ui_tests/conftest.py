import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect, Page, BrowserContext

load_dotenv()

auth_user = os.getenv('AUTH_BASIC_USER')
auth_password = os.getenv('AUTH_BASIC_PASSWORD')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": auth_user,
            "password": auth_password
        },
        'base_url' : os.getenv('UI_URL'), #->     page.goto('https://qauto.forstudy.space/panel/garage')
    }


@pytest.fixture(scope="function")
def ui_login_multy(context: BrowserContext):
    def _new_window():

        page : Page = context.new_page()
        is_open = len(context.pages) == 1
        if is_open:
            page.goto('/')
            page.locator('//button[@class="btn btn-outline-white header_signin"]').click()
            page.get_by_role("textbox", name="Email").fill(login)
            assert page.get_by_role("textbox", name="Email").input_value() == login  # check if input field is fill 'STR'
            page.get_by_role("textbox", name="Password").fill(password)
            assert page.get_by_role("textbox", name="Password").input_value() == password
            with page.expect_response('/api/auth/signin') as response_info:
                page.get_by_role("button", name="Login").click()
            response = response_info.value
            assert response.status == 200

            element_notify = page.locator('//div[@class="alert alert-success"]/p')
            expect(element_notify).to_have_text("You have been successfully logged in")
            assert element_notify.inner_text() == "You have been successfully logged in"
            page.reload()
        return page
    return _new_window

# @pytest.fixture(scope="function")
# def ui_login(page: Page):
#     page.goto('/')
#     page.locator('//button[@class="btn btn-outline-white header_signin"]').click()
#     page.get_by_role("textbox", name="Email").fill(login)
#     assert page.get_by_role("textbox", name="Email").input_value() == login  # check if input field is fill 'STR'
#     page.get_by_role("textbox", name="Password").fill(password)
#     assert page.get_by_role("textbox", name="Password").input_value() == password
#     with page.expect_response('/api/auth/signin') as response_info:
#         page.get_by_role("button", name="Login").click()
#     response = response_info.value
#     assert response.status == 200
#
#     element_notify = page.locator('//div[@class="alert alert-success"]/p')
#     expect(element_notify).to_have_text("You have been successfully logged in")
#     assert element_notify.inner_text() == "You have been successfully logged in"
#     page.reload()
#     return page
#     #https://qauto.forstudy.space -> [, 'qauto.forstudy.space]
#     # context = browser.new_context()
#     # create a new page inside context.
#     # page = context.new_page()
#     # login: guest
#     # pass: welcome2qauto
#     # page.goto(f"https://{auth_user}:{auth_password}@{base_url.split('https://')[1]}/")
#
#
#     # page.get_by_role("button", name="Sign In").click()
#     # page.locator("button.btn.btn-outline-white.header_signin").click()
#
#     # expect(element_notify).to_be_hidden() | fix -> page.reload()



@pytest.fixture
def del_car(context: BrowserContext):
    car_ids_list: list = []
    yield car_ids_list
    for car_id in car_ids_list:
        response_delete = context.request.delete(f'api/cars/{car_id}')
        if response_delete.status == 200:
            print(f"Successfully deleted car {car_id}")
        else:
            print(f'something went wrong with status code {response_delete.status}')
