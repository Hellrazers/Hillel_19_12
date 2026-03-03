import pytest

from contract.cars.cars import Cars
from tests.api_tests.api_client import ApClients
from tests.lesson_12_tests.mock_tests import APIClient


@pytest.fixture(scope='module')
def api_base():
    return ApClients()



@pytest.fixture
def create_cars(api_base):
    api = Cars(api_base)
    data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    response = api.post_cars(json=data)
    assert response.status_code == 201
    car_id = response.json()['data']['id']

    yield api_base, car_id, response

    response_delete = api.delete_car_by_id(car_id)
    assert response_delete.status_code == 200
