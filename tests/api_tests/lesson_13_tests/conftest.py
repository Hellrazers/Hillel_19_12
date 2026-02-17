import logging
import os
import sys
import pathlib
import pytest
import requests
from dotenv import load_dotenv

# load_dotenv()
logger = logging.getLogger("tests.fixtures")
# logger.propagate = False

logger_request = logging.getLogger("tests.request")
load_dotenv()
BASE_URL = os.getenv("API_URL", 'https://qauto.forstudy.space/')
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


@pytest.fixture
def auth_login():
    print(f"platform.system(): {sys.platform.system()}")
    print(f"os.name: {os.name}")
    print(f"sys.platform: {sys.platform}")
    logger.info('-'*80)
    logger.info('Setting up OUR FIXTURE[get_car]')
    logger.info('-'*80)
    print(BASE_URL)
    print(LOGIN)
    print(PASSWORD)
    content = {'email': LOGIN, 'password': PASSWORD, 'remember': 'false'}

    logger.info(f'request')

    response = requests.post(f'{BASE_URL}api/auth/signin', json=content)
    assert response.status_code == 200, "Content was not created"
    headers = {'Autroeization': "Bearer token_256"}
    return response, headers


USER_CREDENTIALS = {
"email": LOGIN,
"password": PASSWORD,
"remember": 'false'
}
CAR_CREDENTIALS = {
  "carBrandId": 1,
  "carModelId": 1,
  "mileage": 122
}
# AUTH = ("guest", "welcome2qauto")


@pytest.fixture
def api():
    logger.info(f"platform.system(): {sys.platform}")
    logger.info(f"os.name: {os.name}")
    logger.info(f"sys.platform: {sys.platform}")
    logger.info('-'*80)
    logger.info('Setting up OUR FIXTURE[api]')
    logger.info('-'*80)
    logger.info(f'Request on URL {BASE_URL}api/auth/signin with Method: POST')
    response = requests.post(f'{BASE_URL}api/auth/signin', json=USER_CREDENTIALS)
    logger.info(f'Status code: {response.status_code}')
    if response.status_code == 400:
        logger.critical(f'Cannot loggin wrong credential')
        raise
    assert response.status_code == 200, "Content was not created"
    yield {"Cookie": f"sid={response.cookies['sid']}"}
    logger.info('-'*80)
    logger.info('Close  OUR FIXTURE[api]')
    logger.info('-'*80)
    logger_request.info(f'Request on URL {BASE_URL}api/auth/logout with Method: GET')
    response = requests.get(f'{BASE_URL}api/auth/logout')
    logger_request.info(f'Status code: {response.status_code}')


@pytest.fixture
def add_car_and_delete(api):
    headers = api
    logger.info('-'*80)
    logger.info('Setting up OUR FIXTURE[add_car_and_delete]')
    logger.info('-'*80)
    logger.info(f'Request on URL {BASE_URL}api/cars with Method: POST with credential: {CAR_CREDENTIALS}')
    response_car = requests.post(f'{BASE_URL}api/cars', json=CAR_CREDENTIALS, headers=headers)
    logger.info(f'Status code: {response_car.status_code} and response {response_car.json()['data']}')
    assert response_car.status_code == 201, "Content was not created"
    car_id = response_car.json()['data'].get('id')
    yield headers, response_car, car_id
    logger.info('-'*80)
    logger.info('Close  OUR FIXTURE[add_car_and_delete]')
    logger.info('-'*80)
    logger.info(f'Request on URL {BASE_URL}api/cars/{car_id} with Method: DELETE')
    response_car_delete = requests.delete(f'{BASE_URL}api/cars/{car_id}', headers=headers)
    logger.info(f'Status code: {response_car.status_code}')
    assert response_car_delete.status_code == 200


@pytest.fixture
def get_car(api):
    logger.info('-'*80)
    logger.info('Setting up OUR FIXTURE[get_car]')
    logger.info('-'*80)
    headers = api
    logger_request.info(f'Request on URL {BASE_URL}/api/cars with Method: GET')
    response = requests.get(f'{BASE_URL}/api/cars',  headers=headers)
    logger_request.info(f'Status code: {response.status_code}')
    assert response.status_code == 200, "Content was not created"
    return headers


@pytest.fixture
def setup_logging():
    logger.info('-'*80)
    logger.info('Setting up OUR FIXTURE')
    logger.info('-'*80)

    handler = logging.StreamHandler(sys.stdout)
    CAR_CREDENTIALS = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }

    return CAR_CREDENTIALS, '123', 123