from selenium.webdriver.common.by import By
from Helpers.lib import Helper
class LetsKodeitMainPage(Helper):
    open_alert = (By.ID, 'alertbtn')
    hide_btn = (By.ID, 'hide-textbox')
    element_locator = (By.ID, "displayed-text")
    hover_btn = (By.XPATH, '//button[@id="mousehover"]')
    top_btn = (By.XPATH, '//a[@href="#top"]')
    footer = (By.XPATH, "//p[contains(@class, 'jqCopyRight')]")
    signin_btn = (By.XPATH, '//a[@href="/login"]')

    def get_element_attribute(self): 
        try:
            self.test_logger.info("Checking the element attribute after Hide...")
            self.wait_and_click(self.hide_btn)
            hide_attr = self.wait_and_get_attribute(self.inp_exapmle, 'style')
            self.test_logger.info(f'Hidden attribute is - {hide_attr}')
            return hide_attr
        except Exception as e:
            self.test_logger.error(f"An error occurred during the Hide/Attribute check. {e}")
            raise

    def hover_and_click(self):
        try:
            self.test_logger.info("Hover and click #top....")
            self.scroll_to_element(self.hover_btn)
            self.wait_and_click(self.hover_btn)
            self.wait_and_click(self.top_btn)
            self.test_logger.info('Mouse hover check passed')

        except Exception as e:
            self.test_logger.error(f"An error occurred during the hover/top click. {e}")
            raise
            

    def get_footer_text(self):
        try:
            self.test_logger.info("Reading the footer text....")
            self.scroll_to_element(self.footer) 
            f_text = self.wait_and_get_text(self.footer)
            self.test_logger.info(f"Footer text is {f_text}")
            return f_text

        except Exception as e:
            self.test_logger.error(f"An error occurred while reading the footer text. {e}")
            raise
    
    def click_sign_in_btn(self):
        try:
            self.wait_and_click(self.signin_btn)
            self.test_logger.info('Clicked sign in button')
        except Exception as e:
            self.test_logger.error(f'Click sign in button failed: {e}')
            raise