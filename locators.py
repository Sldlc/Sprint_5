from selenium.webdriver.common.by import By


class Locators:
    #регистрация аккаунта
    REG_NAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'
    REG_EMAIL = By.XPATH, './/label[text()="Email"]/following-sibling::input'
    REG_PASSWORD = By.XPATH, './/input[@name="Пароль"]'
    BUTTON_REGISTRATION = By.XPATH, '//button[text() = "Зарегистрироваться"]'
    BUTTON_LOGIN_REG = By.XPATH, '//a[text() = "Войти"]'
    NOTIFICATION_INCORRECT_PASSWORD = By.XPATH, '//p[text() = "Некорректный пароль"]'

    #аутентификация
    AUTH_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    AUTH_PASSWORD = By.XPATH, '//input[@name = "Пароль"]'
    BUTTON_LOGIN_AUTH = By.XPATH, '//button[text()="Войти"]'
    BUTTON_REGISTRATION_AUTH = By.XPATH, '//a[text() = "Зарегистрироваться"]'
    BUTTON_RESTORE_PASSWORD = By.XPATH, '//a[text() = "Восстановить пароль"]'
    BUTTON_LOGIN_RESTORE_PASSWORD = By.XPATH, '//a[text() = "Войти"]'

    #личный кабинет
    PROFILE = By.XPATH, '//a[@href = "/account/profile"]'
    ORDERS_HISTORY = By.XPATH, '//a[@href = "/account/order-history"]'
    LOGOUT = By.XPATH, '//button[@type = "button"]'

    #главная страница
    CONSTRUCTOR_ON_HEADER = By.XPATH, '//p[text() = "Конструктор"]'
    ORDER_FEED_ON_HEADER = By.XPATH, '//p[text() = "Лента Заказов"]'
    LOGO_STELLAR_BURGER = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//p[text() = "Личный Кабинет"]'
    BUTTON_LOGIN_ON_START_PAGE = By.XPATH, './/button[text() = "Войти в аккаунт"]'
    BUTTON_BUNS = By.XPATH, '//span[text() = "Булки"]'
    BUTTON_SAUCES = By.XPATH, '//span[text() = "Соусы"]'
    BUTTON_FILLINGS = By.XPATH, '//span[text() = "Начинки"]'
    BUTTON_MAKE_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'
    CHOSEN_SELECTOR = By.XPATH, '//div[@class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'
