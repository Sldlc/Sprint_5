
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *
from helpers import *



class TestRegistration:

    def test_registration_new_account_success_submit(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION_AUTH))
        driver.find_element(*Locators.BUTTON_REGISTRATION_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_REGISTRATION))
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_AUTH))
        assert driver.find_element(*Locators.BUTTON_LOGIN_AUTH).is_displayed()

    def test_notification_for_incorrect_password(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION_AUTH))
        driver.find_element(*Locators.BUTTON_REGISTRATION_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_REGISTRATION))
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys('qw123')
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.NOTIFICATION_INCORRECT_PASSWORD).is_displayed()

    def test_registration_name_is_empty_failed(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION_AUTH))
        driver.find_element(*Locators.BUTTON_REGISTRATION_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_REGISTRATION))
        driver.find_element(*Locators.REG_NAME).send_keys('')
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.BUTTON_REGISTRATION).is_displayed()

    def test_registration_without_domain_failed(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ON_START_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_REGISTRATION_AUTH))
        driver.find_element(*Locators.BUTTON_REGISTRATION_AUTH).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_REGISTRATION))
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys('r123yandex.ru')
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.BUTTON_REGISTRATION).is_displayed()

