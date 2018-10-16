import pytest

from pages.LoginPage import LoginPage


def test_login(selenium):
    login = LoginPage(selenium)
    login.login("tomsmith", "SuperSecretPassword!")
    assert login.success_message_present()

def test_login_failed(selenium):
    login = LoginPage(selenium)
    login.login("tom", "SuperSecretPassword!")
    assert login.error_message_present()