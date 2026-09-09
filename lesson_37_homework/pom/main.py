from selenium.webdriver.common.by import By
from Helpers.lib import Helper, ElementHelper

class LetsKodeitMainPage:
    open_alert = (By.ID, 'alertbtn')
    element_locator = (By.ID, "displayed-text")
    hover_btn = (By.XPATH, '//button[@id="mousehover"]')
    top_btn = (By.XPATH, '//a[@href="#top"]')
    footer = (By.XPATH, "//p[contains(@class, 'jqCopyRight')]")

    def __init__(self, browser):
        self.browser = browser
        self.helper = Helper()
        self.element_helper = ElementHelper()


    def save_alert_text_to_file(self, file_name):
        self.browser.find_element(*self.open_alert).click()
        alert_text = self.helper.get_and_accept_alert_text(self.browser)
        self.helper.write_to_file(file_name=file_name, text=alert_text, mode='a+')
        return alert_text

    def get_element_attribute(self, file_name):
        web_elem = self.browser.find_element(*self.element_locator)
        self.browser.execute_script("arguments[0].style.display = 'none';", web_elem)
        style_value = web_elem.get_attribute("style")
        self.helper.write_to_file(file_name=file_name, text=style_value, mode='a+')

    def hover_and_click_top(self):
        self.element_helper.scroll_to_element(self.browser, self.hover_btn)
        self.element_helper.hover_element(self.browser, self.hover_btn)
        top_elem = self.element_helper.wait_for_element_visible(self.browser, self.top_btn)
        top_elem.click()

    def write_footer_text(self, file_name):
        footer_elem = self.browser.find_element(*self.footer)
        self.browser.execute_script("arguments[0].scrollIntoView();", footer_elem)
        footer_text = footer_elem.text
        self.helper.write_to_file(file_name=file_name, text=footer_text, mode='a+')