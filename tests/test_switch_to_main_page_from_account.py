from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *


class TestSwitchToConstructor:

    def test_switch_to_constructor_by_logo(self, driver, login):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.LOGO_STELLAR_BURGER).click()
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_switch_to_constructor_by_constructor_button(self, driver, login):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR_ON_HEADER).click()
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()
