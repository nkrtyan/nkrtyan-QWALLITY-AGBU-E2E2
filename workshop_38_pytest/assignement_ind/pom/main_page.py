from selenium.webdriver.common.by import By
from workshop_38_pytest.assignement_ind.helpers import Helper

class Letskodeit_main_page(Helper):
    alert_btn = (By.XPATH, '//input[@id = "alertbtn"]')
    hide_show_element = (By.XPATH, '//input[@id = "displayed-text"]')
    hide_btn = (By.ID, "hide-textbox")
    changed_attribute = (By.ID, "displayed-text")
    mouse_hove_btn = (By.XPATH, '//button[@id = "mousehover"]')
    mouse_btn_top = (By.XPATH, '//a[text()= "Top"]')
    scroll_footer = (By.XPATH, "//div[contains(@class, 'footer')]//p")
    btn_sign_in = (By.XPATH, "//h1[text()='Practice Page']//preceding::a[text()='Sign In']")


    def hide_show_function(self):
        try:
        
            self.find_and_click(self.hide_show_element)
            hide_attr = self.get_attribute(self.changed_attribute, 'style')
            self.test_logger.info(f'Hidden attribute is - {hide_attr}')
            return hide_attr

        except Exception as e:
            self.test_logger.error(f'Hide element check failed: {e}')
            raise


    def mouse_hover(self):
        try:
            self.find_and_click(self.mouse_hove_btn)
            self.find_and_click(self.mouse_btn_top)
            self.test_logger.info('Mouse hover check passed')

        except Exception as e:
            self.test_logger.error(f'Mouse hover check failed: {e}')
            raise


    def scroll_function(self):
        try:
            f_text = self.get_text(self.scroll_footer)
            self.test_logger.info(f"Footer text is - {f_text}")
            return f_text
        except Exception as e:
            self.test_logger.error(f'Footer text check failed: {e}')
            raise


    def click_sign_in_btn(self):
        try:
            self.find_and_click(self.btn_sign_in)
            self.test_logger.info('Clicked sign in button')
        except Exception as e:
            self.test_logger.error(f'Click sign in button failed: {e}')
            raise
