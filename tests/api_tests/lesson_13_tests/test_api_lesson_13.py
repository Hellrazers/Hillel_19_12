import pytest
import requests

base_url = 'http://127.0.0.1:7070'
content = {'cars': ['Audi, VW', 'Toyota']}
updated_content = {'bikes': ['Honda', 'Suzuki']}

@pytest.fixture
def create_content():
    # PRE _TEST


    print('Creating content...')
    response = requests.post(f'{base_url}/content', json=content)
    assert response.status_code == 200, "Content was not created"

    yield response , 123, [1, 34]
    #POST_TEST
    print('Deleting content...')
    response = requests.delete(f'{base_url}/content/{response.json().get('id')}')
    assert response.status_code == 200, "Unable delete content"





def test_get_content(auth_login):
    # assert False
    response, headers = auth_login
    print('Getting content...')
    response_get = requests.get(f'{base_url}/users', headers=headers) #url 'http://127.0.0.1:7070/api/v1/users'
    assert response_get.status_code == 200, "Unable to get content"
    server_content = response_get.json().get('content')







@pytest.fixture
def create_content_1():
    # PRE _TEST

    print('Creating content...')
    response = requests.post(f'{base_url}/content', json=content)
    assert response.status_code == 200, "Content was not created"

    return response, 123, [1, 34]



class TestContent2:

    # def test_add_content(self):
    #     print('Checking content adding...')
    #     response_data = requests.post(f'{base_url}/content', json=content)
    #     assert response_data.status_code == 200, "Content was not created"
    #     assert response_data.json().get('message') == 'Content created successfully!'

    def test_get_content(self, create_content ):
        # assert False
        response, value1, value2 = create_content
        print('Getting content...')
        response_get = requests.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content

    def test_modify_content(self):
        print('Modifying content...')
        response = requests.put(f'{base_url}/content/0', json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    def test_deleting_content(self):
        print('Deleting content...')
        response = requests.delete(f'{base_url}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'























class TestContent:

    @pytest.mark.dependency(name="test_add_content")
    def test_add_content(self):
        print('Checking content adding...')
        response_data = requests.post(f'{base_url}/content', json=content)
        assert response_data.status_code == 200, "Content was not created"
        assert response_data.json().get('message') == 'Content created successfully!'

    @pytest.mark.dependency(depends =["test_add_content"])
    def test_get_content(self):
        print('Getting content...')
        response_get = requests.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content

    @pytest.mark.dependency(depends = ["test_add_content"])
    def test_modify_content(self):
        print('Modifying content...')
        response = requests.put(f'{base_url}/content/0', json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    @pytest.mark.dependency(depends =["test_add_content"])
    def test_deleting_content(self):
        print('Deleting content...')
        response = requests.delete(f'{base_url}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'


