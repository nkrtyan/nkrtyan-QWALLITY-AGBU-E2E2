from selenium.webdriver.common.by import By

from helpers.wait_helper import WaitHelper


class LoginPage:

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")

    # This locator worked in your previous test
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]')

    VALIDATION_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Invalid') "
        "or contains(text(),'incorrect') "
        "or contains(text(),'invalid')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def enter_email(self, email):
        field = self.wait.visible(self.EMAIL)
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.visible(self.PASSWORD)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.clickable(self.LOGIN_BUTTON).click()

    def get_validation_message(self):
        return self.wait.visible(
            self.VALIDATION_MESSAGE
        ).text
