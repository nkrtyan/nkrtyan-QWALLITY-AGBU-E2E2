from selenium.webdriver.common.by import By
from Helpers.lib import Helper
import logging

class LetsKodeitMainPage:
    open_alert = (By.ID, 'alertbtn')
    hide_btn = (By.ID, 'hide-textbox')
    element_locator = (By.ID, "displayed-text")
    hover_btn = (By.XPATH, '//button[@id="mousehover"]')
    top_btn = (By.XPATH, '//a[@href="#top"]')
    footer = (By.XPATH, "//p[contains(@class, 'jqCopyRight')]")

    def __init__(self, browser):
        self.browser = browser
        self.helper = Helper()

    def get_alert_text(self, file_name):
        try:
            logging.info("Click to alert btn...")
            self.helper.wait_for_element_clickable(self.browser, self.open_alert)
            alert_text = self.helper.get_and_accept_alert_text(self.browser, file_name)
            logging.info(f"A text was received from the alert: {alert_text}")
            return alert_text
        except Exception as e:
            logging.error(f"An error accurded from alert {e}")
            raise

    def get_element_attribute(self, file_name):
        try:
            logging.info("Checking the element attribute after Hide...")
            element = self.helper.wait_for_element_visible(self.browser, self.element_locator)
            self.helper.wait_for_element_clickable(self.browser, self.hide_btn)
            style_value = element.get_attribute("style")
            if file_name:
                self.helper.write_to_file(file_name, style_value)
            logging.info(f"Style attribute value {style_value}")
            return style_value
        
        except Exception as e:
            logging.error(f"An error occurred during the Hide/Attribute check. {e}")
            raise

    def hover_and_click(self):
        try:
            logging.info("Hover and click #top....")
            self.helper.scroll_to_element(self.browser, self.hover_btn)
            top_elem = self.helper.wait_for_element_clickable(self.browser, self.top_btn)
            logging.info("Top click is done")

        except Exception as e:
            logging.error(f"An error occurred during the hover/top click. {e}")
            raise
            

    def get_footer_text(self, file_name):
        try:
            logging.info("Reading the footer text....")
            footer_elem = self.helper.scroll_to_element(self.browser, self.footer) 
            footer_text = footer_elem.text
            self.helper.write_to_file(file_name=file_name, text=footer_text, mode='a+')
            logging.info(f"Footer text {footer_text}")
            return footer_text

        except Exception as e:
            logging.error(f"An error occurred while reading the footer text. {e}")
            raise