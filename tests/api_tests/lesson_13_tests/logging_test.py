import logging
import requests



import logging
import logging.config
import yaml




BASE_URL = "https://qauto.forstudy.space/"
AUTH = ("guest", "welcome2qauto")
CAR_CREDENTIALS = {
  "carBrandId": 1,
  "carModelId": 1,
  "mileage": 122
}
logger = logging.getLogger("tests.request")
logger_error = logging.getLogger("tests.error")
logger_error.setLevel(logging.ERROR)


class TestContent:

    def test_signin_with_existence_user(self, setup_logging):
        car_tupple, some_str, some_int = setup_logging
        logger.info(f'Request on URL {BASE_URL} with Method: GET')
        response = requests.get(f'{BASE_URL}', auth=AUTH)
        logger.info(f'Status code: {response.status_code}')
        assert response.status_code == 200, "Content was not created"


    def test_adding_a_car(self, get_car):
        headers = get_car
        logger.info(f'Request on URL {BASE_URL}api/cars with Method: POST with credential: {CAR_CREDENTIALS}')
        response_car = requests.post(f'{BASE_URL}api/cars',json=CAR_CREDENTIALS, auth=AUTH, headers=headers)
        logger.info(f'Status code: {response_car.status_code} and response {response_car.json()['data']}')
        assert response_car.status_code == 201, "Content was not created"
        data_resp = response_car.json()['data']
        assert data_resp['id'] is not None, "Id was not created"
        assert data_resp['brand'] == 'Audi'

        exp_model_str = 'AT'
        if data_resp['model'] != exp_model_str:
            logger_error.error(f'Actual result:{data_resp['model']} not expected to {exp_model_str}')
            raise
        # assert data_resp['model'] == 'TT'
        assert data_resp['carBrandId'] == CAR_CREDENTIALS['carBrandId']
        # assert data_resp['carModelId'] == CAR_CREDENTIALS['modelId']
        assert data_resp['initialMileage'] == CAR_CREDENTIALS['mileage']


    def test_get_car_200(self, add_car_and_delete):
        headers, response_car_post, id_car = add_car_and_delete
        # with open('logging.yaml', 'r') as f:
        #     config = yaml.safe_load(f.read())
        #     logging.config.dictConfig(config)
        # 480760
        logger.info(f'Request on URL {BASE_URL}api/cars/{id_car} with Method: GET ')
        response_car = requests.get(f'{BASE_URL}api/cars/{id_car}', json=CAR_CREDENTIALS, auth=AUTH, headers=headers)
        logger.info(f'Status code: {response_car.status_code} and response {response_car.json()['data']}')
        assert response_car.status_code == 200, "Content was not created"
        #
        # logger_yaml = logging.getLogger(__name__)
        # logger.info("Логування налаштовано через YAML!")
