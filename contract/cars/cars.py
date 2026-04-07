import logging
from dataclasses import asdict

from lib.models.base_pydantic import BaseResponseModel, ListResponseModel
from lib.models.cars.request_car_models import CarRequestPost
from lib.models.cars.response_car_models import CarResponseModel, CarsRespModelPydantic
from lib.response_model import ResponseModel
from tests.api_tests.api_client import ApClients

logger = logging.getLogger('api')




class Cars(ApClients):

    def __init__(self, api_client: ApClients):
        super().__init__()
        self.api_client = api_client
        self.path = '/api/cars'


    def get_car_by_id_py(self, item_id: str):
        resp =  self.api_client._get(endpoint=f'{self.path}/{item_id}')
        resp_valid =  BaseResponseModel[CarsRespModelPydantic].from_response(resp)
        return resp_valid

    def get_cars_py(self, params: dict = None):
        resp = self.api_client._get(endpoint=self.path, params=params)
        resp_valid =  ListResponseModel[CarsRespModelPydantic].from_response(resp)
        return resp_valid

    def post_cars_with_resp_model(self, json:dict =  CarRequestPost()):
        response = self.api_client._post(endpoint=self.path, json_payload=asdict(json))
        # assert response.headers['content-typ'] == ['application/json; charset=utf-8 ']
        return CarResponseModel(ResponseModel(response))

    def post_cars_no_model(self, json:dict =  CarRequestPost()):
        return self.api_client._post(endpoint=self.path, json_payload=asdict(json))

    def put_cars_update_by_id(self, json: dict, item_id: str):
        return self.api_client._put(endpoint=f'{self.path}/{item_id}', json=json)

    def get_cars(self, params: dict = None):
        return self.api_client._get(endpoint=self.path, params=params)

    def get_car_by_id(self, item_id: str):
        return self.api_client._get(endpoint=f'{self.path}/{item_id}')

    def delete_car_by_id(self, item_id: str, exp_code:int = 200):
        response = self.api_client._delete(endpoint=f'{self.path}/{item_id}', exp_code=exp_code)



        return response