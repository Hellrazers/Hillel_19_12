import requests
import unittest
from unittest.mock import patch, Mock


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url



    # get reuest {self.base_url}/data
    def get_data(self):
        url = f"{self.base_url}/data"
        # base_url = https://api.example.com
        # url = https://api.example.com/data
        response = requests.get(url) #patch post put del
        return response.json() if response.status_code == 200 else None # 201, 404 ,500 return None
        # if response.status_code == 200:
        #     return response.json()
        # else:
        #     return None

#/users/{id}
#postitive -succcess
#negative - 404 - id not found
# negative - 409 `! 200



class TestAPIClient(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        # Створюємо макет відповіді API-ендпоінта
        # mock_response = Mock()
        # status_code = 200
        # json.return_value = {'data': 'example_data'}

        # https: // api.example.com / data get
        # put payload {
        # delate // api.example.com / data / {ID}
        # {
        #     'data': [
        #         {
        #             user : id
        #             Is_delted /...
        #         }
        #     ]
        # }

        # Встановлюємо макет для функції get() з бібліотеки requests
        # mock_get.return_value = mock_response

        # Тестуємо метод get_data() з класу APIClient
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()

        # # Перевіряємо, чи метод get() був викликаний з очікуваним URL
        # mock_get.assert_called_once_with('https://api.example.com/data')

        # Перевіряємо результат
        self.assertEqual(result, {'data': 'example_data'})

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        # Створюємо макет відповіді API-ендпоінта для
				# симуляції невдачі (status_code != 200)
        mock_response = Mock()
        mock_response.status_code = 404

        # Встановлюємо макет для функції get() з бібліотеки requests
        mock_get.return_value = mock_response

        # Тестуємо метод get_data() з класу APIClient при невдачі
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()

        # Перевіряємо, чи метод get() був викликаний з очікуваним URL
        mock_get.assert_called_once_with('https://api.example.com/data')

        # Перевіряємо, що результат - None при невдачі
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)