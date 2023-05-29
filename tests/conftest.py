from selenium import webdriver
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    time.sleep(3)
    return driver

@pytest.fixture
def fake_name():
    return "Elena"

@pytest.fixture
def fake_email():
    return "test102@yandex.ru"

@pytest.fixture
def fake_password():
    return "1q2w3e"

@pytest.fixture
def fake_wrong_password():
    return "1q2w"
