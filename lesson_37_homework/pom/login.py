
import sys
from pathlib import Path

from Helpers.lib import Helper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helpers.lib import Helper, ElementHelper, WaitHelper, save_to_file, scroll_to_element, hover_element, wait_for_element_visible, open_new_tab_and_switch


class LetsKodeitLoginPage:

    signin_btn = (By.XPATH, '//a[@href="/login"]')

    email_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_login_btn = (By.XPATH, "//button[@id='login']")
    error_msg_locator = (By.XPATH, "//span[@id='incorrectdetails']")
    
    def login_with_invalid_data(self, email, password, file_name):
    
        self.browser.find_element(*self.signin_btn).click()
    
        self.browser.find_element(*self.email_input).send_keys(email)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.submit_login_btn).click()
    
        error_elem = wait_for_element_visible(self.browser, self.error_msg_locator)
        validation_message = error_elem.text
        Helper.save_to_file(text=validation_message, file_name=file_name)
    
    def open_google_in_new_tab(self):
    
        open_new_tab_and_switch(self.browser, "https://www.google.com/")