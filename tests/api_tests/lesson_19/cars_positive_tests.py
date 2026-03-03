import pytest
import requests

from contract.cars.cars import Cars


def test_get_user_profile(api_base):
    api = api_base
    response = api._get(endpoint='/api/users/profile')
    assert response.status_code == 200


def test_create_car_post(api_base):
    api = Cars(api_base)

    response = api.post_cars()
    assert response.status_code == 201
    car_id = response.json()['data']['id']

    response_car_by_id = api.get_car_by_id(car_id)
    assert response_car_by_id.status_code == 200


    response_delete = api.delete_car_by_id(car_id)
    assert response_delete.status_code == 200


    response_car_by_id_after_delete = api.get_car_by_id(car_id)
    assert response_car_by_id_after_delete.status_code == 404


def test_create_car_get_with_fix(create_cars):
    api_base, car_id, _ = create_cars
    api = Cars(api_base)
    response_car_by_id = Cars(api_base).get_car_by_id(car_id)
    assert response_car_by_id.status_code == 200
    assert response_car_by_id.json()['data']['id'] == car_id
    assert response_car_by_id.json()['data']['carBrandId'] == 1
    assert response_car_by_id.json()['data']['carModelId'] == 1
    assert response_car_by_id.json()['data']['initialMileage'] == 122


# def test_get_user_(api_base):
#     api = api_base
#     response = api._get(endpoint='/api/cars')
#     assert response.status_code == 200
#
#
# def test_get_expenses(api_base):
#     api = api_base
#     # response = api._get(endpoint='/api/expenses?carId=480760')
#     response = api._get(endpoint='/api/expenses', params={"carId":480760 , 'car': "bugatti", "list_obg": [1, 2, 3]})
#     assert response.status_code == 200
