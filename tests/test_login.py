import pytest
import conftest
from locators import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import login
from data import Data

def test_login_main(driver):
    """Вход по кнопке «Войти в аккаунт» на главной"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL)) != None

def test_login_lk(driver):
    """Вход через кнопку «Личный кабинет»"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainMenuLocators.LK_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL)) != None

def test_login_reg(driver):
    """Вход через кнопку в форме регистрации"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.REG_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL)) != None


def test_login_error_password(driver):
    """Вход с неправильным паролем"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.WRONG_PASSWORD)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.ERROR_PASSWORD)) != None

def test_login_restore(driver):
    """Вход через кнопку в форме восстановления пароля"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.RESTORE_PASSWORD_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RestorePasswordLocators.LOGIN_BUTTON)).click()
    login(driver, Data.EMAIL, Data.PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.MAIN_LABEL))
    driver.find_element(*MainMenuLocators.LK_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LkLocators.MAIN_LABEL)) != None
