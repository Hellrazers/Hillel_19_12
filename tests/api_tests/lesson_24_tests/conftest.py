import pytest

from contract.expenses.expenses import Expenses


# @pytest.fixture
# def delete_expenses_after_test(api_base):
#     yield
#
#     api = Expenses(api_base)
#     response_delete = api.delete_expenses_by_id(expenses_id)
#     assert response_delete.status_code == 200