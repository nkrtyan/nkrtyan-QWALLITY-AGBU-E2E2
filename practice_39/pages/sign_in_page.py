from selenium.webdriver.common.by import By
from lib.helpers import Helper
from testdata import test_data


class SignIn(Helper):

    email_txt = (By.ID, "email")
    pass_txt = (By.ID, "login-password")
    login_btn = (By.ID, "login")
    invalid_msg = (By.ID, "incorrectdetails")

    def sign_in(self):
        try:
            self.find_and_send_keys(self.email_txt, test_data.email_data)
            self.find_and_send_keys(self.pass_txt, test_data.pass_data)
            self.find_and_click(self.login_btn)
            validation_msg = self.get_text(self.invalid_msg)
            self.test_logger.info(f"Validation message: {validation_msg}")

            return validation_msg

        except Exception as e:
            self.test_logger.error(
                f"Sign in failed: {e}"
            )
            raise