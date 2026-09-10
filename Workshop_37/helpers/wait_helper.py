from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:

    def __init__(self, driver, timeout=10):
        self.wait = WebDriverWait(driver, timeout)

    def presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def alert(self):
        return self.wait.until(
            EC.alert_is_present()
        )
