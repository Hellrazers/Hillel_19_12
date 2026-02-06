import pytest
from assertpy import assert_that
import sys


def add_func(a , b):
    return  a + b

def div_func(a , b):
    return  a / b

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (15, 11, 11),
    (5, 6, 11),
])
@pytest.mark.regression
@pytest.mark.positive
@pytest.mark.smoke
def test_add_first(a, b, result):
    actual_result = add_func(a, b)
    expected_result = result

    assert_that(expected_result  , "If somethjing was wrong its shows ").is_equal_to(actual_result)


@pytest.mark.parametrize("some_value", [
    (2, 3, 0.6666666666666666),
    (15, 0, 26),
    (5, 6, 0.8333333333333334),
])
@pytest.mark.regression
@pytest.mark.positive
@pytest.mark.smoke
def test_add_second(some_value):
    a, b, result = some_value
    actual_result = None
    if b != 0:
        actual_result = div_func(a, b)
    else:
        raise ZeroDivisionError
    expected_result = result

    assert_that(expected_result  , "If somethjing was wrong its shows ").is_equal_to(actual_result)


@pytest.mark.parametrize("age", [
    {'value': 25},
    {'value': 35},
    # {'name': 'Anna'},
])
@pytest.mark.parametrize("some_value", [
    {'name': 'Ivan'},
    {'name': 'Ivan', 'age': 25},
    # {'name': 'Anna'},
])
@pytest.mark.regression
@pytest.mark.positive
@pytest.mark.smoke
def test_add_second(some_value, age):
    name  = some_value.get('name')
    value  = age.get('value')

    assert_that(name).is_equal_to('Ivan')
    assert_that(value).is_equal_to(25)
    assert True

# @pytest.mark.regression
# @pytest.mark.positive
# @pytest.mark.smoke
# def test_add_second():
#     actual_result = add_func(5, 5)
#
#     expected_result = 10
#
#     assert_that(expected_result, "If somethjing was wrong its shows ").is_equal_to(actual_result)




class TestSomeClass():

    some_value = None


    @pytest.mark.positive
    @pytest.mark.regression
    def test_second(self):
        assert True
        __class__.some_value = 5

    @pytest.mark.positive
    @pytest.mark.regression
    def test_class_value(self):
        print(__class__.some_value)



# /users  get post