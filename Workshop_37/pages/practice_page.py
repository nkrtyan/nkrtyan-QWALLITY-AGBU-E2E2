from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticePage:

    # Locators
    ALERT_BUTTON = (By.ID, "alertbtn")

    HIDE_BUTTON = (By.ID, "hide-textbox")
    HIDDEN_ELEMENT = (By.ID, "displayed-text")

    MOUSE_HOVER = (By.ID, "mousehover")
    TOP_LINK = (By.XPATH, "//a[text()='Top']")

    FOOTER = (By.TAG_NAME, "footer")

    SIGN_IN = (
        By.XPATH,
        '//*[@id="navbar-inverse-collapse"]/span[2]/div/div/a'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------------------------
    # Alert
    # -------------------------

    def click_alert_button(self):
        self.driver.find_element(*self.ALERT_BUTTON).click()

    def get_alert_text(self):
        alert = self.wait.until(
            EC.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    # -------------------------
    # Hide Element
    # -------------------------

    def hide_element(self):
        self.driver.find_element(*self.HIDE_BUTTON).click()

        return self.driver.find_element(
            *self.HIDDEN_ELEMENT
        )

    # -------------------------
    # Mouse Hover
    # -------------------------

    def click_top_from_mouse_hover(self):
        mouse_hover = self.driver.find_element(
            *self.MOUSE_HOVER
        )

        ActionChains(self.driver).move_to_element(
            mouse_hover
        ).perform()

        self.wait.until(
            EC.element_to_be_clickable(self.TOP_LINK)
        ).click()

    # -------------------------
    # Footer
    # -------------------------

    def get_footer_text(self):
        return self.driver.find_element(
            *self.FOOTER
        ).text

    # -------------------------
    # Sign In
    # -------------------------

    def click_sign_in(self):
        sign_in = self.wait.until(
            EC.presence_of_element_located(self.SIGN_IN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            sign_in
        )

        self.driver.execute_script(
            "arguments[0].click();",
            sign_in
        )