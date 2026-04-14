from dataclasses import asdict

from lib.models.expenses.request_expenses_models import ExpensesRequestPost
from lib.models.expenses.response_expenses_models import ExpensesResponseModel, ExpenseResponseModel
from lib.response_model import ResponseModel
from tests.api_tests.api_client import ApClients
import allure

class Expenses(ApClients):

    def __init__(self, api_client: ApClients):
        super().__init__()
        self.api_client = api_client
        self.path = '/api/expenses'

    @allure.step('GET expenses all')
    def get_expenses(self, params: dict):
        return ExpensesResponseModel(ResponseModel(self.api_client._get(endpoint=self.path, params=params)))

    @allure.step('Post expenses by id: {item_id}')
    def post_expenses(self, json_data: ExpensesRequestPost):
        response = self.api_client._post(endpoint=self.path, json_payload=json_data)
        return ExpenseResponseModel(ResponseModel(response))



    def delete_expenses_by_id(self, item_id: str, exp_code:int = 200):
        response = self.api_client._delete(endpoint=f'{self.path}/{item_id}', exp_code=exp_code)
        return ExpenseResponseModel(ResponseModel(response))