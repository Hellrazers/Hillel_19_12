from playwright.sync_api import Page

from pages.base_model import Base_page


class Garage_model(Base_page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = '/panel/garage'
        self.api_path = '/api/cars'
        self.button_add_car_locator = page.get_by_role('button', name='Add car')
        self.input_miles =  page.locator('//input[@name="miles"]')
        #MODAL
        self.modal_select_car_brand = page.locator('#addCarBrand')
        self.modal_select_car_model = page.locator('#addCarModel')
        self.modal_select_car_miles = page.locator('#addCarMileage')
    #
    def go_to(self):
        self.navigate(self.path)
    #
    # def go_to(self):
    #     self.page.goto(self.path)

    def click_button_add_car_and_chose_car(self, *args):
        car_brand, car_model, car_miles = args
        self.button_add_car_locator.click()
        self.modal_select_car_brand.select_option(car_brand)
        bwm_text = (self.modal_select_car_brand.evaluate
                    ("el => el.options[el.selectedIndex].text"))

        assert bwm_text == car_brand
        self.modal_select_car_model.select_option(car_model)
        assert (self.modal_select_car_model.evaluate
                ("el => el.options[el.selectedIndex].text") == car_model)

        self.modal_select_car_miles.fill(car_miles)

    def return_id_while_modal_click_button_add(self):
        with self.page.expect_response(self.api_path) as response_info:
            self.modal_add_button.click()
        response = response_info.value
        assert response.status == 201
        return response.json()['data']['id']

    def len_of_car_miles(self):
        return len(self.input_miles.all())

