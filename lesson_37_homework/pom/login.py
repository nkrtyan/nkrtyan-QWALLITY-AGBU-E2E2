from selenium.webdriver.common.by import By
from Helpers.lib import Helper
from TestData import config

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
        self.helper.scroll_to_element(self.browser, self.signin_btn)
        self.helper.wait_for_element_clickable(self.browser, self.signin_btn, action="click")


        email_field = self.helper.wait_for_element_clickable(self.browser, self.email_input)
        email_field.send_keys(username)
        password_field = self.helper.wait_for_element_clickable(self.browser, self.password_input)
        password_field.send_keys(password)

        # self.helper.wait_for_element_clickable(self.browser, self.email_input, action="send_keys", text=username)
        # self.helper.wait_for_element_clickable(self.browser, self.password_input, action="send_keys", text=password)
        self.helper.wait_for_element_clickable(self.browser, self.submit_login_btn, action="click")

        # self.browser.find_element(*self.email_input).send_keys(username)
        # self.browser.find_element(*self.password_input).send_keys(password)
        # self.browser.find_element(*self.submit_login_btn).click()

        error_elem = self.helper.wait_for_element_visible(self.browser, self.error_msg_locator)
        error_text = error_elem.text
        self.helper.write_to_file(file_name=file_name, text=error_text) 

    def open_google_in_new_tab(self):
        self.helper.open_new_tab_and_switch(self.browser, config.new_tab_url) #FIXED move url to config