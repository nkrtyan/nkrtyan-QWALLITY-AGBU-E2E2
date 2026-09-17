import os
import allure
from functools import wraps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def error_handler(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)

        except Exception as e:
            self.test_logger.error(f"{func.__name__}: {e}")

            os.makedirs(self.test_logger.screenshot_dir, exist_ok=True)

            self.driver.save_screenshot(
                f"{self.test_logger.screenshot_dir}/"
                f"{self.test_logger.test_name}.png"
            )

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Failure",
                attachment_type=allure.attachment_type.PNG
            )

            raise

    return wrapper


class Helper:

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    @error_handler
    def go_to_page(self, url, new_window=False):
        if new_window:
            self.driver.switch_to.new_window("tab")

        self.driver.get(url)

    @error_handler
    def switch_window(self, window_id=0):
        self.driver.switch_to.window(
            self.driver.window_handles[window_id]
        )

    @error_handler
    def find_and_click(self, locator):
        element = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    @error_handler
    def find_and_send_keys(self, locator, text):
        element = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.visibility_of_element_located(locator)
        )

        element.send_keys(text)

    @error_handler
    def get_text(self, locator):
        element = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    @error_handler
    def get_attribute(self, locator, attribute):
        element = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.presence_of_element_located(locator)
        )

        return element.get_attribute(attribute)

    @error_handler
    def accept_alert(self, timeout=5):
        alert = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.alert_is_present()
        )

        alert_text = alert.text
        alert.accept()

        self.test_logger.info(
            f"Alert text: {alert_text}"
        )

        return alert_text

    @error_handler
    def append_text_to_file(self, file_path, text):
        with open(
            file_path,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(text + "\n")