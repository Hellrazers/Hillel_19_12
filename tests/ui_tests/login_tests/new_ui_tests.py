import pytest

from playwright.sync_api import Page


def test_ui_login(ui_login):
    page: Page = ui_login
    page.goto("/panel/expenses")
    assert 1 == 1