from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *


class TestSwitchSectionsInConstructor:
    def test_switch_to_fillings_block_from_buns(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_ON_START_PAGE))
        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.CHOSEN_SELECTOR).text == "Начинки"

    def test_switch_to_fillings_from_sauces(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_ON_START_PAGE))
        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        driver.find_element(*Locators.BUTTON_SAUCES).click()
        assert driver.find_element(*Locators.CHOSEN_SELECTOR).text == "Соусы"

    def test_switch_to_buns_from_fillings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_ON_START_PAGE))
        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        driver.find_element(*Locators.BUTTON_BUNS).click()
        assert driver.find_element(*Locators.CHOSEN_SELECTOR).text == "Булки"

    def test_switch_to_sauces_from_buns_being_auth(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_MAKE_ORDER))
        driver.find_element(*Locators.BUTTON_SAUCES).click()
        assert driver.find_element(*Locators.CHOSEN_SELECTOR).text == "Соусы"
