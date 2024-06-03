from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *


class TestEnterToPersonalAccount:

    def test_enter_to_personal_account(self, driver, login):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        assert driver.find_element(*Locators.ORDERS_HISTORY).is_displayed()
