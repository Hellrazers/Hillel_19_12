import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect, Page

load_dotenv()

auth_user = os.getenv('AUTH_BASIC_USER')
auth_password = os.getenv('AUTH_BASIC_PASSWORD')
base_url = os.getenv('UI_URL')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": auth_user,
            "password": auth_password
        }
    }



@pytest.fixture(scope="function")
def ui_login(page: Page):
    #https://qauto.forstudy.space -> [, 'qauto.forstudy.space]
    # context = browser.new_context()
    # create a new page inside context.
    # page = context.new_page()
    # login: guest
    # pass: welcome2qauto
    # page.goto(f"https://{auth_user}:{auth_password}@{base_url.split('https://')[1]}/")

    page.goto(base_url)
    # page.get_by_role("button", name="Sign In").click()
    # page.locator("button.btn.btn-outline-white.header_signin").click()
    page.locator('//button[@class="btn btn-outline-white header_signin"]').click()
    page.get_by_role("textbox", name="Email").fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    page.get_by_role("button", name="Login").click()
    element_notify = page.locator('//div[@class="alert alert-success"]/p')
    expect(element_notify).to_have_text("You have been successfully logged in")
    assert element_notify.inner_text() == "You have been successfully logged in"

    return page