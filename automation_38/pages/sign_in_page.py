from selenium.webdriver.common.by import By
from lib.helpers import Helper


class SignInPage(Helper):

    txt_email = (By.ID, "email")
    txt_pass = (By.ID, "login-password")
    btn_login = (By.ID, "login")
    msg_invalid = (By.ID, "incorrectdetails")

    def login_with_invalid_credentials(self, email, password):
        try:
            self.find_and_send_keys(self.txt_email, email)
            self.find_and_send_keys(self.txt_pass, password)
            self.find_and_click(self.btn_login)
            self.test_logger.info('Submitted invalid login credentials')
        except Exception as e:
            self.test_logger.error(f'Login failed: {e}')
            raise

    def get_validation_message(self):
        try:
            validation_msg = self.get_text(self.msg_invalid, 5)
            self.test_logger.info(f'Validation Message is - {validation_msg}')
            return validation_msg
        except Exception as e:
            self.test_logger.error(f'Get validation message failed: {e}')
            raise

    def open_google_in_new_tab(self, google_url):
        try:
            self.go_to_page(google_url, new_window=True)
            self.switch_window(1)
            current_url = self.driver.current_url
            self.test_logger.info(f'Opened google in new tab: {current_url}')
            return current_url
        except Exception as e:
            self.test_logger.error(f'Open google in new tab failed: {e}')
            raise
