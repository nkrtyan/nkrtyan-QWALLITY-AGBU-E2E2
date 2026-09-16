from Helpers.lib import Helper
from selenium.webdriver.common.by import By
from TestData import data

class LetsKodeitLoginPage(Helper):
  email_input = (By.XPATH, "//input[@name='email']")
  password_input = (By.XPATH, "//input[@name='password']")
  submit_login_btn = (By.XPATH, "//button[@id='login']")
  error_msg_locator = (By.XPATH, "//span[@id='incorrectdetails']")


  def login(self):
    try:
        self.test_logger.info(f"Trying to login in by {data.username} user...")
        self.wait_and_send_keys(self.email_input, data.username)
        self.wait_and_send_keys(self.password_input, data.password)
        self.wait_and_click(self.submit_login_btn)
        self.test_logger.info("Login btn clicked")

        error_text = self.wait_and_get_text(self.error_msg_locator,5)
        self.test_logger.info(f"The text of the error received '{error_text}'")
        return error_text
    except Exception as e:
      self.test_logger.error(f"An error occurred during the login flow. {e}")
      raise
