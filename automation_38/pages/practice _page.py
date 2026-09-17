from selenium.webdriver.common.by import By
from lib.helpers import Helper


class PracticePage(Helper):

    title = (By.XPATH, "//title[text()='Practice Page']")
    btn_alert = (By.ID, "alertbtn")
    btn_hide = (By.ID, "hide-textbox")
    inp_example = (By.ID, "displayed-text")
    btn_mousehover = (By.ID, "mousehover")
    btn_top = (By.LINK_TEXT, "Top")
    footer = (By.CLASS_NAME, "jqCopyRight")
    btn_sign_in = (
        By.XPATH,
        "//a[contains(@href, '/login') or contains(@href, '/sign_in')]"
        " | //a[normalize-space()='Sign In' or normalize-space()='Login']"
        " | //button[normalize-space()='Sign In' or normalize-space()='Login']"
        " | //input[@value='Sign In' or @value='Login']",
    )

    def open_alert_and_get_text(self):
        try:
            self.find_and_click(self.btn_alert)
            alert_text = self.accept_alert()
            self.test_logger.info(f"Alert text - {alert_text}")
            return alert_text
        except Exception as e:
            self.test_logger.error(f"Open alert and get text failed: {e}")
            raise

    def hide_element_and_get_visibility_attribute(self):
        try:
            self.find_and_click(self.btn_hide)
            hide_attr = self.get_attribute(self.inp_example, "style")
            self.test_logger.info(f"Hidden attribute is - {hide_attr}")
            return hide_attr
        except Exception as e:
            self.test_logger.error(f"Hide element check failed: {e}")
            raise

    def hover_and_click_top(self):
        try:
            self.find_and_click(self.btn_mousehover)
            self.find_and_click(self.btn_top)
            self.test_logger.info("Hover and click top passed")
        except Exception as e:
            self.test_logger.error(f"Hover and click top failed: {e}")
            raise

    def get_footer_text(self):
        try:
            f_text = self.get_text(self.footer)
            self.test_logger.info(f"Footer text is - {f_text}")
            return f_text
        except Exception as e:
            self.test_logger.error(f"Footer text check failed: {e}")
            raise

    def click_sign_in(self):
        try:
            self.append_text_to_file("my_logs.txt", "Starting click_sign_in method...")
            element = self.driver.find_element(*self.btn_sign_in)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
            self.test_logger.info("Clicked sign in button")
            self.append_text_to_file("my_logs.txt", "Clicked sign in button successfully")
        except Exception as e:
            self.test_logger.error(f"Click sign in button failed: {e}")
            raise
