import time
import pytest
import conftest
from locators import LoginLocators
from locators import ConstructorLocators
from locators import MainMenuLocators
from locators import RegistrationLocators
from locators import RestorePasswordLocators
from selenium import webdriver
from data import Data

def test_login_main(driver):
    driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    passwordField = driver.find_element(*LoginLocators.PASSWORD_INPUT)
    passwordField.send_keys(Data.PASSWORD)
    time.sleep(3)
    value = passwordField.get_attribute('value')
    assert len(value) == 6

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.MAIN_LABEL) != None

def test_login_lk(driver):
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.MAIN_LABEL) != None

def test_login_reg(driver):
    driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*RegistrationLocators.MAIN_LABEL) != None

    driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.MAIN_LABEL) != None

def test_login_error_password(driver):
    driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Data.WRONG_PASSWORD)
    time.sleep(3)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.ERROR_PASSWORD) != None

def test_login_restore(driver):
    driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.RESTORE_PASSWORD_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*RestorePasswordLocators.MAIN_LABEL) != None

    driver.find_element(*RestorePasswordLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Data.EMAIL)
    time.sleep(3)

    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Data.PASSWORD)
    time.sleep(3)

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.MAIN_LABEL) != None
