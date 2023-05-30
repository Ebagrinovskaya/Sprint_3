import time
import pytest
import conftest
from locators import Locators
from selenium import webdriver

def test_go_to_lk(fake_email, fake_password, driver):
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

    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LK_PAGE_MAIN_LABEL) != None

def test_go_to_constructor_from_lk(fake_email, fake_password, driver):
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

    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LK_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.MAIN_MENU_CONSTRUCTOR_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

def test_logout(fake_email, fake_password, driver):
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

    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LK_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LK_PAGE_LOGOUT_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None
