from dataclasses import asdict

from lib.models.cars.request_car_models import CarRequestPost
from tests.api_tests.api_client import ApClients


class Cars(ApClients):

    def __init__(self, api_client: ApClients):
        super().__init__()
        self.api_client = api_client
        self.path = '/api/cars'

    def post_cars(self, json:dict =  CarRequestPost()):

        return self.api_client._post(endpoint=self.path, json=asdict(json))

    def put_cars_update_by_id(self, json: dict, item_id: str):
        return self.api_client._put(endpoint=f'{self.path}/{item_id}', json=json)

    def get_cars(self, params: dict):
        return self.api_client._get(endpoint=self.path, params=params)

    def get_car_by_id(self, item_id: str):
        return self.api_client._get(endpoint=f'{self.path}/{item_id}')

    def delete_car_by_id(self, item_id: str):
        return self.api_client._delete(endpoint=f'{self.path}/{item_id}')