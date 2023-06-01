import pytest
import conftest
from locators import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from data import Data
from login_page import *
from registration_page import *

def test_register(driver):
    """Регистрация с корректным паролем"""
    faker = Faker()
    email = faker.email()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.LK_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.REG_BUTTON)).click()
    register(driver, faker.name(), email, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.LK_BUTTON)).click()
    login(driver, email, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.LK_BUTTON)).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL)) != None

def test_register_error(driver):
    """Регистрация с некорректным паролем"""
    faker = Faker()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.LK_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.REG_BUTTON)).click()

    register(driver, faker.name(), faker.email(), Data.WRONG_PASSWORD)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationLocators.ERROR_PASSWORD)) != None
