import time
import pytest
import conftest
from locators import Locators
from selenium import webdriver

def test_login_main(fake_email, fake_password, driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(fake_email)
    time.sleep(3)

    passwordField = driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT)
    passwordField.send_keys(fake_password)
    time.sleep(3)
    value = passwordField.get_attribute('value')
    assert len(value) == 6

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

    driver.close()
    time.sleep(3)

def test_login_lk(fake_email, fake_password, driver):
    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(fake_email)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(fake_password)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

    driver.close()
    time.sleep(3)

def test_login_reg(fake_email, fake_password, driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_REG_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.REG_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.REG_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(fake_email)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(fake_password)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

    driver.close()
    time.sleep(3)

def test_login_error_password(fake_email, fake_wrong_password, driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(fake_email)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(fake_wrong_password)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_ERROR_PASSWORD) != None

    driver.close()
    time.sleep(3)

def test_login_restore(fake_email, fake_password, driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_RESTORE_PASSWORD_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.RESTORE_PASSWORD_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.RESTORE_PASSWORD_PAGE_LOGIN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(fake_email)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(fake_password)
    time.sleep(3)

    driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

    driver.close()
    time.sleep(3)
