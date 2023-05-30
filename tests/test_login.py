import time
import pytest
import conftest
from locators import Locators
from selenium import webdriver
from data import Data

def test_login_main(driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    passwordField = driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT)
    passwordField.send_keys(Data.PASSWORD)
    time.sleep(3)
    value = passwordField.get_attribute('value')
    assert len(value) == 6

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

def test_login_lk(driver):
    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

def test_login_reg(driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.REG_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.REG_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

def test_login_error_password(driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(Data.WRONG_PASSWORD)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_ERROR_PASSWORD) != None

def test_login_restore(driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_RESTORE_PASSWORD_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.RESTORE_PASSWORD_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.RESTORE_PASSWORD_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None
