from app.Helpers.logger import get_logger
logger = get_logger(__name__)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page object for the Sign In / Login form."""

    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'login-password')
    LOGIN_BTN = (By.ID, 'login')
    VALIDATION_MSG = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/span')

    DEFAULT_TIMEOUT = 10

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, self.DEFAULT_TIMEOUT)

    def login(self, email, password):
        # 10. Fill the fields with incorrect email or password and click LogIn
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_field.click()
        email_field.send_keys(email)

        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_field.click()
        password_field.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def get_validation_message(self):
        # 11. Get validation message (explicit wait, per the workshop's note)
        message = self.wait.until(EC.visibility_of_element_located(self.VALIDATION_MSG))
        return message.text
