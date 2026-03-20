import json
import logging
import os
import requests
from dotenv import load_dotenv
from tests.utils import log_request

load_dotenv()
logger = logging.getLogger("test")

class ApClients:
    def __init__(self):
        self.base_url = os.getenv('UI_URL')
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')
        self.session = requests.Session()
        self.__token = None

    def _authenticate(self):
        if self.__token is None:
            self.get_token()
        self.session.headers.update({"Cookie": f"sid={self.__token}"})

    def get_token(self):
        user_creads = {
            "email": self.login,
            "password": self.password,
            "remember": False
        }
        response = requests.post(f'{self.base_url}/api/auth/signin', json=user_creads)
        assert response.status_code == 200, "Something problem with token"
        self.__token = response.cookies['sid']

    @log_request
    def _get(self, endpoint, params: dict = None):
        self._authenticate()
        # base_url = https://qauto.forstudy.space
        #endpoint = /api/users/current
        our_path= f'{self.base_url}{endpoint}'
        # logger.info(f"-> Method: GET | url: {our_path}")
        response = self.session.get(our_path, params=params)

        return response

    @log_request
    def _post(self, endpoint, json_payload=None):
        self._authenticate()
        our_path= f'{self.base_url}{endpoint}'
        # logger.info(f"-> Method: POST | url: {our_path} | payload: {json.dumps(json_payload)} {json_payload}")
        response = self.session.post(f'{our_path}', json=json_payload)
        # if response.status_code in [200, 201]:
        #     logger.info(f"<- Status code: {response.status_code} | response time : {response.elapsed.total_seconds() * 1000} ms")
        # else:
        #     logger.info(
        #         f"<- Status code: {response.status_code} | Error message: '{response.json().get('message')}' | response time : {response.elapsed.total_seconds() * 1000} ms")
        return response

    @log_request
    def _put(self, endpoint, json=None):
        self._authenticate()

        return self.session.put(f'{self.base_url}{endpoint}', json=json)

    @log_request
    def _delete(self, endpoint, exp_code = 200):
        self._authenticate()
        response = self.session.delete(f'{self.base_url}{endpoint}')
        assert response.status_code == exp_code, "Something problem with token"


        return response
