import time
import pytest
import conftest
from locators import Locators
from selenium import webdriver

def test_constructor(driver):
    driver.find_element(*Locators.CONSTRUCTOR_PAGE_TOPPING_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_TOPPING_DIV) != None

    driver.find_element(*Locators.CONSTRUCTOR_PAGE_SAUCE_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_SAUCE_DIV) != None

    driver.find_element(*Locators.CONSTRUCTOR_PAGE_ROLL_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*Locators.CONSTRUCTOR_PAGE_ROLL_DIV) != None

    driver.close()
    time.sleep(3)

