from app.Helpers.logger import get_logger
logger = get_logger(__name__)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticePage:
    """Page object for https://www.letskodeit.com/practice"""

    # ---- Locators (class attributes as (By, value) tuples) ----
    ALERT_BTN = (By.XPATH, '//input[@id="alertbtn"]')
    DISPLAYED_TEXT_INPUT = (By.XPATH, '//input[@id="displayed-text"]')
    HIDE_BTN = (By.XPATH, '//input[@id="hide-textbox"]')
    HIDDEN_ELEMENT = (By.XPATH, '//input[starts-with(@style, "display:")]')
    MOUSE_HOVER_BTN = (By.XPATH, '//button[@id="mousehover"]')
    TOP_LINK = (By.XPATH, '//a[text()="Top"]')
    FOOTER_TEXT = (By.XPATH, "/html/body/div[1]/div[3]/div/span/div/div[1]/div/div[1]/p")
    SIGN_IN_BTN = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/span[2]/div/div/a')

    DEFAULT_TIMEOUT = 40

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, self.DEFAULT_TIMEOUT)

   
    def open_alert(self):
        self.wait.until(EC.element_to_be_clickable(self.ALERT_BTN)).click()

    def get_and_accept_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def hide_displayed_text(self):
        self.wait.until(EC.element_to_be_clickable(self.HIDE_BTN)).click()

    def get_hidden_element_style(self):
        element = self.wait.until(EC.presence_of_element_located(self.HIDDEN_ELEMENT))
        return element.get_attribute("style")

    def hover_mouse_and_click_top(self):
        mouse_hover_btn = self.wait.until(EC.element_to_be_clickable(self.MOUSE_HOVER_BTN))
        mouse_hover_btn.click()
        top_link = self.wait.until(EC.visibility_of_element_located(self.TOP_LINK))
        ActionChains(self.browser).move_to_element(top_link).perform()

    def scroll_to_footer_and_get_text(self):
        footer = self.wait.until(EC.presence_of_element_located(self.FOOTER_TEXT))
        self.browser.execute_script("arguments[0].scrollIntoView();", footer)
        self.wait.until(EC.visibility_of(footer))
        return footer.text

    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_BTN)).click()
