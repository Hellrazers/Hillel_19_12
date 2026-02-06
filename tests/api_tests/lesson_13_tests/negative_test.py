import sys

import pytest
from assertpy import assert_that


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.skipif(sys.modules == 'Win32', reason='If our system is Windows our test never run')
def test_skip_if():
    actual_result = 2 + 2
    expected_result = 4
    #TODO is here fix assert
    assert_that(expected_result  , "If somethjing was wrong its shows ").is_equal_to(actual_result)
    # assert True


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.xfail(reason='this our reason why test is broken')
def test_fail():
    actual_result = 2 + 2
    expected_result = 4
    #TODO is here fix assert
    assert_that(expected_result  , "If somethjing was wrong its shows ").is_equal_to(actual_result)

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.skip(reason='https://jira-sever/TASK-1')
def test_skip():
    actual_result = 2 + 2
    expected_result = 4
    #TODO is here fix assert
    assert_that(expected_result  , "If somethjing was wrong its shows ").is_equal_to(actual_result)
    # assert True