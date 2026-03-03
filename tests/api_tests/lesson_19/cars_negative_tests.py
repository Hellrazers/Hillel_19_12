import pytest

from contract.cars.cars import Cars
from faker import Faker

fake = Faker(locale='uk_UA')

@pytest.mark.negative
def test_create_car_404(api_base):
    car_id = 1231231231
    api = Cars(api_base)
    response_car_by_id = api.get_car_by_id(car_id)
    assert response_car_by_id.status_code == 404



def test_faker():
    print(fake.first_name())
    print(fake.email())
    print(fake.name())