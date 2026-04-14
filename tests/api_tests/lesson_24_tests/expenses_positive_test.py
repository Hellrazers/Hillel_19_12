from dataclasses import asdict
import allure
import pytest

from Lessons.lesson_6.for_example import response
from contract.expenses.expenses import Expenses
from lib.models.expenses.request_expenses_models import ExpensesRequestPost

@pytest.fixture
def cleanup_expenses(api_base):
    # Створюємо список, куди будемо записувати ID для видалення
    expense_ids = []
    api = Expenses(api_base)

    # Передаємо список у тест
    yield expense_ids

    # Код після yield виконається НАВІТЬ якщо тест впаде (AssertionError)
    for exp_id in expense_ids:
        print(f"\nОчищення: видалення витрати з ID {exp_id}")
        api.delete_expenses_by_id(exp_id)

@allure.epic("Expenses")
@allure.link('https://lms.ithillel.ua/groups/68d16268736be2a264d809a9/lessons/68d16268736be2a264d809d9?article_id=691dae0ad0e616179bac26f9',
             name='EPIC: 123')
@allure.feature("Expenses API")
@allure.link('https://lms.ithillel.ua/groups/68d16268736be2a264d809a9/lessons/68d16268736be2a264d809d9?article_id=691dae0ad0e616179bac26f9',
             name='Feature: 123')
class TestExpensesTags:
    pass



class TestExpenses(TestExpensesTags):
    @staticmethod
    @allure.story("GET expenses by ID ")
    @allure.title("GET: list of all expenses by id")
    @allure.description('''We try to get expenses by id and check it''')
    @allure.severity(allure.severity_level.MINOR)
    def test_get_all_expenses_by_id(api_base):
        with allure.step('We create pre-condition before test'):
            api = Expenses(api_base)
            car_id = 492243
        response_get = api.get_expenses(params={"carId": car_id, "page": 1})
        with allure.step('We validate response after reqeusest '):
            assert response_get.status_code == 200
            rsp_data = response_get.data
            for expense in rsp_data:
                assert expense.carId == car_id
                assert expense.id is not None


    @staticmethod
    @allure.story("GET expenses by ID ")
    @allure.description('''We try to get expenses by id and check it''')
    @allure.severity(allure.severity_level.MINOR)
    def test_get_all_expenses_by_id_dynamic_title(api_base):
        api = Expenses(api_base)
        car_id = 492243
        allure.dynamic.title(f'GET: list of all expenses by {car_id}')
        response_get = api.get_expenses(params={"carId": car_id, "page": 1})
        assert response_get.status_code == 200
        rsp_data = response_get.data
        for expense in rsp_data:
            assert expense.carId == car_id
            assert expense.id is not None

    # TODO Спробуйте пофіксите
    @staticmethod
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("POST expenses")
    @allure.link('https://lms.ithillel.ua/groups/68d16268736be2a264d809a9/lessons/68d16268736be2a264d809d9?article_id=691dae0ad0e616179bac26f9',
                 name='Story: 123')
    @allure.title("POST: create new expense")
    def test_post_expenses(create_cars, cleanup_expenses):
        """
        We try to create new expense and validate expsenses response
        """
        api_base, car_id, _ = create_cars
        api = Expenses(api_base)
        # json_request = ExpensesRequestPost(
        #     carId = car_id,
        #     mileage = 1500,
        #     liters = 1500,
        #     totalCost = 123
        # )
        # json_2= asdict(json_request)

        # додайте параметрезацію
        # reportedAt -> використовуючи дейтайм на теперішній день
        json_valid = {'carId': 492243, 'forceMileage': False, 'liters': 1500, 'mileage': 1500, 'reportedAt': "2026-03-20",
                      'totalCost': 123}
        response_get = api.post_expenses(json_valid)
        assert response_get.status_code == 200
        rsp_data = response_get.data

    # дописати асьорти

        cleanup_expenses.append(rsp_data.carId)
    # response_delete = api.delete_expenses_by_id(rsp_data.carId)
    # assert response_delete.status_code == 200

# UI_URL=https://qauto.forstudy.space
# LOGIN=nedzelnytskyidev+hillel02026@gmail.com
# PASSWORD=AYf3JtDQnAcMbnc
# IS_LOGIN_DISABLE=True
