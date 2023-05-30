import time
import pytest
import conftest
from locators import Locators
from selenium import webdriver
from data import Data

def test_go_to_lk(driver):
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

    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LK_PAGE_MAIN_LABEL) != None

def test_go_to_constructor_from_lk(driver):
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

    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LK_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.MAIN_MENU_CONSTRUCTOR_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_MAIN_LABEL) != None

def test_logout(driver):
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

    driver.find_element(*Locators.MAIN_MENU_LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LK_PAGE_MAIN_LABEL) != None

    driver.find_element(*Locators.LK_PAGE_LOGOUT_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.LOGIN_PAGE_MAIN_LABEL) != None
