import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'http://127.0.0.1:7070/auth'

@pytest.fixture
def auth_login():
    content = {'username': 'admin', 'password': 'admin'}
    print(f'{os.environ.get("API_URL")}/auth')
    response = requests.post(f'{BASE_URL}', json=content)
    assert response.status_code == 200, "Content was not created"
    headers = {'Autroeization': "Bearer token_256"}
    return response, headers