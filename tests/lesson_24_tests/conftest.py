import pytest


# session  - >  один раз на весь тест
# module -> один раз на ліректорію
# class -> class
# function  -> один раз за фуунцію
#
#
# @pytest.fixture(scope="session")
# def app(client):
#     pass
#
# @pytest.fixture(scope="function")
# def client():
#     pass


@pytest.fixture(scope="session")
def app():
    pass

@pytest.fixture()
def client(app):
    print("test client")


@pytest.fixture(autouse=True , scope="session")
def session():
    print("AUTOUSE SESION START ")
    yield
    print("AUTOUSE SESION ")


@pytest.fixture()
def my_first_fixture():
    print("my_first_fixture from lesson 24")



