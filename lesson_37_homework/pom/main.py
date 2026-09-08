import sys
from pathlib import Path

from Helpers.lib import Helper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helpers.lib import Helper, ElementHelper, WaitHelper, save_to_file, scroll_to_element, hover_element, wait_for_element_visible, open_new_tab_and_switch

class LetsKodeitMainPage:

    open_alert = (By.ID, 'alertbtn')
    element = (By.ID, "displayed-text")
    hover_btn = (By.XPATH, '//button[@id="mousehover"]')
    top_btn = (By.XPATH, '//a[@href="#top"]')
    footer = (By.XPATH,"//p[contains(@class, 'jqCopyRight')]")
    signin_btn = (By.XPATH, '//a[@href="/login"]')

    email_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_login_btn = (By.XPATH, "//button[@id='login']")
    error_msg_locator = (By.XPATH, "//span[@id='incorrectdetails']")

    def __init__(self, browser):
        self.browser = browser

    def save_alert_text_to_file(self, file_name):
                
        self.browser.find_element(*self.open_alert).click()
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        
        Helper.save_to_file(text=alert_text, file_name=file_name)
        
        return alert_text

    def get_element_attribute(self, file_name):
       
        self.browser.find_element(*self.element)
        self.execute_script("arguments[0].style.display = 'none';",self.element)
        
        style_value = self.element.get_attribute("style")

        Helper.save_to_file(text=style_value, file_name=file_name)

    def hover_and_click_top(self):
        ElementHelper.scroll_to_element(self.browser, self.hover_btn)
        ElementHelper.hover_element(self.browser, self.hover_btn)
        self.browser.find_element(*self.top_btn).click()


    def write_footer_text(self, file_name):

        footer = self.browser.find_element(*self.footer)

        self.browser.execute_script("arguments[0].scrollIntoView();",footer)

        footer_text = footer.text

        Helper.save_to_file(text=footer_text, file_name=file_name)



    