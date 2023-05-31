from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from locators import *
from urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.STELLAR_BURGERS)
    yield driver
    driver.quit()

def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

def register(driver, name, email, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys(name)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.REG_BUTTON).click()