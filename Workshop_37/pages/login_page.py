from selenium.webdriver.common.by import By


class LoginPage:

    # Locators
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login")
    VALIDATION_MESSAGE = (By.ID, "incorrectdetails")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_validation_message(self):
        return self.driver.find_element(
            *self.VALIDATION_MESSAGE
        ).text