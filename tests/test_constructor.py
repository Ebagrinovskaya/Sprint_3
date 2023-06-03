import pytest
import conftest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_constructor_topping(driver):
    """Открытие начинок"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.TOPPING_BUTTON)).click()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.TOPPING_DIV)) != None

def test_constructor_sauce(driver):
    """Открытие соусов"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.SAUCE_BUTTON)).click()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.SAUCE_DIV)) != None

def test_constructor_roll(driver):
    """Открытие булок"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.TOPPING_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.TOPPING_DIV))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.ROLL_BUTTON)).click()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.ROLL_DIV)) != None
