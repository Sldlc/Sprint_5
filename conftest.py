import pytest
from selenium import webdriver
from data import UserAuthData
from locators import Locators


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
    driver.find_element(*Locators.AUTH_EMAIL).send_keys(UserAuthData.my_email)
    driver.find_element(*Locators.AUTH_PASSWORD).send_keys(UserAuthData.my_password)
    driver.find_element(*Locators.BUTTON_LOGIN_AUTH).click()
