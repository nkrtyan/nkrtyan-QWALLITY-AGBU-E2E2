from selenium.webdriver.common.by import By
from Helpers.lib import Helper, ElementHelper

class LetsKodeitLoginPage:
    signin_btn = (By.XPATH, '//a[@href="/login"]')
    email_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_login_btn = (By.XPATH, "//button[@id='login']")
    error_msg_locator = (By.XPATH, "//span[@id='incorrectdetails']")

    def __init__(self, browser):
        self.browser = browser
        self.helper = Helper()
        self.element_helper = ElementHelper()

    def login_with_invalid_data(self, email, password, file_name):
        self.element_helper.scroll_to_element(self.browser, self.signin_btn)
        signin_elem = self.element_helper.wait_for_element_clickable(self.browser, self.signin_btn)
        signin_elem.click()

        self.browser.find_element(*self.email_input).send_keys(email)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.submit_login_btn).click()

        error_elem = self.element_helper.wait_for_element_visible(self.browser, self.error_msg_locator)
        validation_message = error_elem.text
        self.helper.write_to_file(file_name=file_name, text=validation_message, mode='a+')

    def open_google_in_new_tab(self):
        self.helper.open_new_tab_and_switch(self.browser, "https://www.google.com/")