from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
