from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    
    # Locators
   

    EMAIL = (
        By.ID,
        "login"
    )

    PASSWORD = (
        By.ID,
        "login-password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login')]"
    )

    ERROR_MESSAGE = (
        By.ID,
        "incorrectdetails"
    )

    
    # Constructor
    

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

   
    # Enter Email
    

    def enter_email(self, email):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

        field.click()

        field.send_keys(
            email
        )

    
    # Enter Password
    

    def enter_password(self, password):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        field.click()

        field.send_keys(
            password
        )

    
    # Click Login
   

    def click_login(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        button.click()

    
    # Get Error Message
    

    def get_error_message(self):

        message = self.wait.until(
            EC.presence_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return message.get_attribute(
            "innerText"
        )