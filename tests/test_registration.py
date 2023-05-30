import time
import pytest
import conftest
from locators import MainMenuLocators
from locators import LoginLocators
from locators import RegistrationLocators
from selenium import webdriver
from faker import Faker
from data import Data

def test_register(driver):
    faker = Faker()
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*RegistrationLocators.MAIN_LABEL) != None

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(faker.name())
    time.sleep(3)

    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(faker.email())
    time.sleep(3)

    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*RegistrationLocators.REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

def test_register_error(driver):
    faker = Faker()
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*RegistrationLocators.MAIN_LABEL) != None

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(faker.name())
    time.sleep(3)

    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(faker.email())
    time.sleep(3)

    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(Data.WRONG_PASSWORD)
    time.sleep(3)

    driver.find_element(*RegistrationLocators.REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*RegistrationLocators.ERROR_PASSWORD) != None
