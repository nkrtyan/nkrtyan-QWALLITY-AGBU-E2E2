from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from helpers.wait_helper import WaitHelper


class PracticePage:

    ALERT_BUTTON = (By.ID, "alertbtn")
    HIDE_ELEMENT = (By.ID, "displayed-text")
    MOUSE_HOVER = (By.ID, "mousehover")
    TOP_OPTION = (By.XPATH, "//a[text()='Top']")
    FOOTER = (By.TAG_NAME, "footer")
    SIGN_IN = (By.XPATH, "//a[contains(text(),'Sign In')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def click_alert_button(self):
        self.wait.clickable(self.ALERT_BUTTON).click()

    def get_alert_text_and_accept(self):
        alert = self.wait.alert()

        text = alert.text

        alert.accept()

        return text

    def hide_element(self):
        element = self.wait.presence(self.HIDE_ELEMENT)

        self.driver.execute_script(
            "arguments[0].style.display = 'none';",
            element
        )

        return element

    def click_top_from_mouse_hover(self):
        mouse_hover = self.wait.visible(self.MOUSE_HOVER)

        ActionChains(self.driver).move_to_element(mouse_hover).perform()

        self.wait.clickable(self.TOP_OPTION).click()

    def get_footer_text(self):
        footer = self.wait.presence(self.FOOTER)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            footer
        )

        return footer.text

    def click_sign_in(self):
        self.wait.clickable(self.SIGN_IN).click()
