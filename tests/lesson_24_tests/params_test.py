import pytest


# @pytest.fixture(params=[1])
# def my_fixture(request):
#     param_value = request.param
#     print(f"Setup with param value: {param_value}")
#     return param_value * 2
# #pytest.mark.parametrize
# # Приклад використання фікстури у тесті
# def test_using_fixture(my_fixture):
#     print(f"Test with fixture value: {my_fixture}")
#     assert my_fixture % 2 == 0




# fixture 1 -> fixture -> test (params) = fixture 1 не побачить праметри
@pytest.fixture()
def pre_fixture_2(request, tmpdir):
    param_value = request.param
    return param_value

@pytest.fixture()
def my_fixture_2(pre_fixture_2):
    param_value = pre_fixture_2
    print(param_value)
    print(f"Setup with param value: {param_value}")
    if isinstance(param_value, dict):
        return param_value.get("name") * 2
    return param_value * 2


# @pytest.mark.parametrize('my_fixture_2', [{"name": 1, 'value': 2}, [1, 2, 3 ,4], (1,32,213)], indirect=True)
def test_using_fixture_2(my_fixture_2):
    print(f"Test with fixture value: {my_fixture_2}")
    assert my_fixture_2 % 2 == 0

@pytest.fixture()
def my_fixture_3():
    def _my_fixture_3(value, name= None):
        return value * 2
    return _my_fixture_3

@pytest.mark.parametrize('value', [1,2 ,3 ])
def test_using_fixture_3(value, my_fixture_3):
    value_2 = my_fixture_3(value)
    print(f"Test with fixture value: {value_2}")
    assert value_2 % 2 == 0

#open_text, int

list_items  = [{"name": 1, 'value': 2}, 1, 2]

# @pytest.mark.parametrize('my_fixture_2', [k for k in list_items], indirect=True)
@pytest.mark.parametrize('my_fixture_2', range(0,5), indirect=True)

@pytest.mark.parametrize("name_surname", [["alex", 'surname'], ['DEN', 18]])
def test_using_fixture_4(my_fixture_2, name_surname):
    name, value = name_surname
    print(f"Test with fixture value: {my_fixture_2}")
    print(name, value)
    assert my_fixture_2 % 2 == 0



@pytest.fixture(scope='class')
def prepare_database():
    print("Підготовка бази даних...")
    yield
    print("Очищення бази даних...")

@pytest.fixture(scope='class')
def prepare_config():
    print("Підготовка конфігурації...")
    yield
    print("Очищення конфігурації...")


@pytest.mark.usefixtures("prepare_database", "prepare_config")
class TestClassWithMultipleFixtures:
    def test_method1(self):
        print("Тестування методу 1...")

    def test_method2(self):
        print("Тестування методу 2...")

# @pytest.mark.parametrize("name, surname", [["alex", 'surname', 3], ['DEN', 18]])
# # @pytest.mark.parametrize("name_surname", [["alex", 'surname'], ['DEN', 18]])
# def test_using_fixture_4(my_fixture_2, name, surname):
#     name, value = name, surname
#     print(f"Test with fixture value: {my_fixture_2}")
#     print(name, value)
#     assert my_fixture_2 % 2 == 0