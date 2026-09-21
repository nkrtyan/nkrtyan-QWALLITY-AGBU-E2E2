from selenium.webdriver.common.by import By
from lib.helpers import Helper


class PracticePage(Helper):

    page_title = (By.XPATH, "//title[text()='Practice Page']")
    alert_button = (By.ID, "alertbtn")
    hide_button = (By.ID, "hide-textbox")
    example_input = (By.ID, "displayed-text")
    mouse_hover_button = (By.ID, 'mousehover')
    top_link = (By.XPATH, "//button[@id='mousehover']//following::a[text()='Top']")
    footer_element = (By.XPATH, "//div[contains(@class, 'footer')]//p")
    sign_in_button = (By.XPATH, "//h1[text()='Practice Page']//preceding::a[text()='Sign In']")

    def check_hide_element(self):
        try:
            self.find_and_click(self.hide_button)
            hidden_style = self.get_attribute(self.example_input, 'style')
            self.test_logger.info(f'Hidden attribute is - {hidden_style}')
            return hidden_style
        except Exception as e:
            self.test_logger.error(f'Hide element check failed: {e}')
            raise

    def check_mouse_hover(self):
        try:
            self.find_and_click(self.mouse_hover_button)
            self.find_and_click(self.top_link)
            self.test_logger.info('Mouse hover check passed')
        except Exception as e:
            self.test_logger.error(f'Mouse hover check failed: {e}')
            raise

    def get_footer_text(self):
        try:
            footer_value = self.get_text(self.footer_element)
            self.test_logger.info(f'Footer text is - {footer_value}')
            return footer_value
        except Exception as e:
            self.test_logger.error(f'Footer text check failed: {e}')
            raise

    def click_sign_in(self):
        try:
            element = self.driver.find_element(*self.sign_in_button)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
            element.click()
            self.test_logger.info('Clicked sign in button')
        except Exception as e:
            self.test_logger.error(
                f'Click sign in button failed: {e}'
            )
            raise