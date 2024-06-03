from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *
from data import *


class TestAuthentication:

    def test_auth_by_click_button_login_on_start_page(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_AUTH))
        driver.find_element(*Locators.REG_EMAIL).send_keys(UserAuthData.my_email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(UserAuthData.my_password)
        driver.find_element(*Locators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_MAKE_ORDER))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_auth_by_click_button_personal_account(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_AUTH))
        driver.find_element(*Locators.REG_EMAIL).send_keys(UserAuthData.my_email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(UserAuthData.my_password)
        driver.find_element(*Locators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_MAKE_ORDER))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_auth_via_registration_page(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_AUTH))
        driver.find_element(*Locators.BUTTON_REGISTRATION_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION))
        driver.find_element(*Locators.BUTTON_LOGIN_REG).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_AUTH))
        driver.find_element(*Locators.REG_EMAIL).send_keys(UserAuthData.my_email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(UserAuthData.my_password)
        driver.find_element(*Locators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_MAKE_ORDER))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_auth_via_restore_password_button(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_AUTH))
        driver.find_element(*Locators.BUTTON_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_RESTORE_PASSWORD))
        driver.find_element(*Locators.BUTTON_LOGIN_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_LOGIN_AUTH))
        driver.find_element(*Locators.REG_EMAIL).send_keys(UserAuthData.my_email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(UserAuthData.my_password)
        driver.find_element(*Locators.BUTTON_LOGIN_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_MAKE_ORDER))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

