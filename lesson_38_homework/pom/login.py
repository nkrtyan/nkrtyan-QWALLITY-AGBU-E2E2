from Helpers.lib import Helper
from selenium.webdriver.common.by import By
from TestData import config
import logging

class LetsKodeitLoginPage:
  signin_btn = (By.XPATH, '//a[@href="/login"]')
  email_input = (By.XPATH, "//input[@name='email']")
  password_input = (By.XPATH, "//input[@name='password']")
  submit_login_btn = (By.XPATH, "//button[@id='login']")
  error_msg_locator = (By.XPATH, "//span[@id='incorrectdetails']")

  def __init__(self, browser):
    self.browser = browser
    self.helper = Helper()

  def login(self, username, password, file_name):
    try:
        logging.info(f"Trying to login in by {username} user...")
        self.helper.scroll_to_element(self.browser, self.signin_btn)
        self.helper.wait_for_element_clickable(self.browser, self.signin_btn)
        logging.info("SignIn btn clicked")

        self.helper.send_keys(self.browser, self.email_input, username)
        self.helper.send_keys(self.browser, self.password_input, password)
        self.helper.wait_for_element_clickable(self.browser, self.submit_login_btn)
        logging.info("Login btn clicked")

        error_elem = self.helper.wait_for_element_visible(
            self.browser, self.error_msg_locator
        )

        error_text = error_elem.text
        self.helper.write_to_file(file_name=file_name, text=error_text)
        logging.info(f"The text of the error received '{error_text}'")
        return error_text
    except Exception as e:
      logging.error(f"An error occurred during the login flow. {e}")
      raise

  def open_new_tab(self):
    try:
        logging.info("Opening Google in a new tab...")
        self.helper.open_new_tab_and_switch(self.browser, config.new_tab_url)
        logging.info("New tab is succesfuly open")
    except Exception as e:
        logging.error(f"An error occured during the new tab open {e}")
        raise