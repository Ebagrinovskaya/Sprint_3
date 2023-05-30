import time
import pytest
import conftest
from locators import MainMenuLocators
from locators import LoginLocators
from locators import ConstructorLocators
from locators import LkLocators
from selenium import webdriver
from data import Data

def test_go_to_lk(driver):
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

    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LkLocators.MAIN_LABEL) != None

def test_go_to_constructor_from_lk(driver):
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

    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LkLocators.MAIN_LABEL) != None

    driver.find_element(*MainMenuLocators.CONSTRUCTOR_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.MAIN_LABEL) != None

def test_logout(driver):
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

    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LkLocators.MAIN_LABEL) != None

    driver.find_element(*LkLocators.LOGOUT_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*LoginLocators.MAIN_LABEL) != None
