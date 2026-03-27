import pytest
from playwright.sync_api import Page, expect

from dotenv import load_dotenv

load_dotenv()


def test_ui(ui_login):
    page: Page = ui_login
    len_of_cars = len(page.locator('//input[@name="miles"]').all())
    page.get_by_role('button', name='Add car').click()
    # page.wait_for_timeout(3000)
    page.locator('//div[@class="modal-content"]//button[@class="btn btn-primary"]').evaluate(
        "el => el.style.border = '5px solid red'")
    page.locator('#addCarBrand').select_option('BMW')
    bwm_text = page.locator('#addCarBrand').evaluate("el => el.options[el.selectedIndex].text")
    assert bwm_text == "BMW"
    # model 3
    # page_locator_add_car = page.locator('#addCarModel').evaluate("el => el.options[el.selectedIndex].text")
    # change model from 3 to x6
    page.locator('#addCarModel').select_option('X6')

    assert page.locator('#addCarModel').evaluate("el => el.options[el.selectedIndex].text") == "X6"
    # assert page_locator_add_car == "X6"
    page.locator('#addCarMileage').fill('1200')
    page.get_by_role('button', name='Add').click()
    # # page.wait_for_timeout(3000)
    # response_get_cars = api.get_cars()
    # assert response_get_cars.status_code == 200
    # page.reload()
    expect(page.locator('//div[@class="alert alert-success"]/p')).to_have_text('Car added')
    len_cars_after_adding = len(page.locator('//input[@name="miles"]').all())

    assert len_cars_after_adding > len_of_cars, f'Count of cars before adding was {len_of_cars}, but now is {len_cars_after_adding}'
