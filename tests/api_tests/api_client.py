import os

import requests
from dotenv import load_dotenv

load_dotenv()

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


    def _get(self, endpoint, params: dict=None):
        self._authenticate()
        return  self.session.get(f'{self.base_url}{endpoint}', params=params)

    def _post(self, endpoint, json=None):
        self._authenticate()

        return self.session.post(f'{self.base_url}{endpoint}', json=json)

    def _put(self, endpoint, json=None):
        self._authenticate()

        return self.session.put(f'{self.base_url}{endpoint}', json=json)

    def _delete(self, endpoint):
        self._authenticate()

        return self.session.delete(f'{self.base_url}{endpoint}')

