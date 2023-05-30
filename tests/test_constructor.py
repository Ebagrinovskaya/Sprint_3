import time
import pytest
import conftest
from locators import ConstructorLocators
from selenium import webdriver

def test_constructor(driver):
    driver.find_element(*ConstructorLocators.TOPPING_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.TOPPING_DIV) != None

    driver.find_element(*ConstructorLocators.SAUCE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.SAUCE_DIV) != None

    driver.find_element(*ConstructorLocators.ROLL_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*ConstructorLocators.ROLL_DIV) != None
