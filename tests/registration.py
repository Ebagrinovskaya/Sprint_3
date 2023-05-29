import time
import pytest
import conftest
from locators import Locators
from selenium import webdriver
from faker import Faker

def test_register(driver):
    faker = Faker()
    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.REG_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.REG_PAGE_NAME_INPUT).send_keys(faker.name())
    time.sleep(3)

    driver.find_element(*Locators.REG_PAGE_EMAIL_INPUT).send_keys(faker.email())
    time.sleep(3)

    driver.find_element(*Locators.REG_PAGE_PASSWORD_INPUT).send_keys("1q2w3e")
    time.sleep(3)

    driver.find_element(*Locators.REG_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.close()
    time.sleep(3)

def test_register_error(driver):
    faker = Faker()
    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.REG_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.REG_PAGE_NAME_INPUT).send_keys(faker.name())
    time.sleep(3)

    driver.find_element(*Locators.REG_PAGE_EMAIL_INPUT).send_keys(faker.email())
    time.sleep(3)

    driver.find_element(*Locators.REG_PAGE_PASSWORD_INPUT).send_keys("1q2w")
    time.sleep(3)

    driver.find_element(*Locators.REG_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.REG_PAGE_ERROR_PASSWORD) != None

    driver.close()
    time.sleep(3)
