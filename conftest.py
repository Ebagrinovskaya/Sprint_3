from selenium import webdriver
import pytest
from urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.STELLAR_BURGERS)
    yield driver
    driver.quit()
