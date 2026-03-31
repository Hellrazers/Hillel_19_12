import pytest
from playwright.sync_api import Page, expect

from dotenv import load_dotenv

from pages.expenses import Expenses_model
from pages.garage_model import Garage_model

load_dotenv()


def test_ui(ui_login, del_car):
    page: Page = ui_login
    list_of_car_ids: list = del_car
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
    # with page.expect_response(lambda response: response.url == "https://qauto.forstudy.space/api/cars" and response.status == 201 and response.request.method == 'POST') as response_info:
    with page.expect_response('/api/cars') as response_info:
        page.get_by_role('button', name='Add').click()
    response = response_info.value
    assert response.status == 201
    # # page.wait_for_timeout(3000)
    # response_get_cars = api.get_cars()
    # assert response_get_cars.status_code == 200
    # page.reload()
    # page.wait_for_timeout(1000)
    car_id_added = response.json()['data']['id']
    #del_car.append(car_id_added)
    list_of_car_ids.append(car_id_added)
    notify_element = page.locator('//div[@class="alert alert-success"]/p')
    expect(notify_element).to_have_text('Car added')
    len_cars_after_adding = len(page.locator('//input[@name="miles"]').all())

    assert len_cars_after_adding > len_of_cars, f'Count of cars before adding was {len_of_cars}, but now is {len_cars_after_adding}'


def test_ui_upgrade(ui_login, del_car):
    car_brand, car_model, car_miles = ['BMW', 'X6', '1200']
    car_list_of_model = ['BMW', 'X6', '1200']
    page: Page = ui_login
    garage_page = Garage_model(page)
    list_of_car_ids: list = del_car
    len_of_cars = garage_page.len_of_car_miles()
    garage_page.click_button_add_car_and_chose_car(*car_list_of_model)

    car_id_added = garage_page.return_id_while_modal_click_button_add()

    list_of_car_ids.append(car_id_added)
    garage_page.notify_verify_text('Car added')

    len_cars_after_adding = garage_page.len_of_car_miles()

    assert len_cars_after_adding > len_of_cars, f'Count of cars before adding was {len_of_cars}, but now is {len_cars_after_adding}'


def test_ui_new_expnceses(ui_login):
    page: Page = ui_login
    expencese_page = Expenses_model(page)

    expencese_page.go_to()
    page.wait_for_timeout(4000)