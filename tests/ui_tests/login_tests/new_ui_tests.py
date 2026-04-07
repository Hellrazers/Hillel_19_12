import time

import pytest

from playwright.sync_api import Page, expect, BrowserContext

from pages.expenses import Expenses_model
from pages.garage_model import Garage_model


def test_dragn_drop(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")

    page.locator("#rect-draggable").drag_to(page.locator("#rect-droppable"))

    expect(page.locator('#text-droppable')).to_contain_text('Dropped!')

def test_iframe(page: Page):
    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page")


    iframe = page.frame_locator('//iframe[@class="embed-responsive-item"]')
    result = iframe.locator('//h1[@class="fw-light"]')
    expect(result).to_contain_text('Album example')
    expect(page.locator('//h1')).to_contain_text('Iframes')
    iframe.locator('//button[@class="navbar-toggler"]').click()
    expect(iframe.locator('//p[@class="text-muted"]')).to_contain_text('Add some information about the album below, the author, or any other background context. Make it a few sentences long so folks can pick up some informative tidbits. Then, link them off to some social networking sites or contact information.')



def test_dialog_alert(page: Page):
    # def dialog_handler(dialog):
    #     assert  1==1
    #     print(dialog.message)
    #     #accept - ok  dismiss - cancel
    #     dialog.accept()
    page.goto("https://www.qa-practice.com/elements/alert/alert")
    page.on("dialog", lambda d: d.accept())
    page.locator("//a[@class='a-button']").click()


def test_ui_upgrade(ui_login_multy, del_car, context: BrowserContext):
    car_brand, car_model, car_miles = ['BMW', 'X6', '1200']
    car_list_of_model = ['BMW', 'X6', '1200']
    page1 = ui_login_multy()
    garage_page = Garage_model(page1)
    page2 = ui_login_multy()
    expences_page = Expenses_model(page2)
    list_of_car_ids: list = del_car
    len_of_cars = garage_page.len_of_car_miles()
    garage_page.click_button_add_car_and_chose_car(*car_list_of_model)

    car_id_added = garage_page.return_id_while_modal_click_button_add()

    list_of_car_ids.append(car_id_added)
    garage_page.notify_verify_text('Car added')

    len_cars_after_adding = garage_page.len_of_car_miles()

    assert len_cars_after_adding > len_of_cars, f'Count of cars before adding was {len_of_cars}, but now is {len_cars_after_adding}'
    page2.close()
    assert 1==1



def test_ui_upgrade(ui_login_multy, context: BrowserContext):
    page = ui_login_multy()
    len_before_click = len(context.pages)
    list_of_pages = []
    for k in range(5):
        page = ui_login_multy()
        list_of_pages.append(page)

    pages = context.pages
    assert len(pages) > len_before_click
    page_last = pages[-1]
    page_last.goto(url="https://github.com/")
    assert page_last.title() == 'GitHub · Change is constant. GitHub keeps you ahead. · GitHub'


def test_ui_uper(ui_login_multy):
    page1 = ui_login_multy()
    page1.goto("/panel/profile")
    str_to_add = 'asdasdasdasd'
    page1.locator('//button[@class="btn btn-primary"]').click()
    page1.locator('#editProfileCountry').click()
    # page1.keyboard.down("Shift")
    page1.keyboard.type(str_to_add)
    for k in range(int(len(str_to_add)/2)):
        page1.keyboard.down("ArrowLeft")

    page1.keyboard.type('ITS TEST', delay=500)
    # page1.keyboard.up("Shift")
    assert 1==1