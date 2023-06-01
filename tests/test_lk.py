import pytest
import conftest
from locators import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from login_page import *

def test_go_to_lk(driver):
    """Переход в личный кабинет"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL)) != None

def test_go_to_constructor_from_lk(driver):
    """Переход в окно конструктора из личного кабинета"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.CONSTRUCTOR_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL)) != None

def test_logout(driver):
    """Разлогинивание"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.MAIN_LABEL))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.LK_BUTTON)).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.MAIN_LABEL)) != None
