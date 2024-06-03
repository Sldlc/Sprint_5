from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *


class TestLogout:
    def test_logout_from_personal_account(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_AUTH))
        assert driver.find_element(*Locators.BUTTON_LOGIN_AUTH).is_displayed()
