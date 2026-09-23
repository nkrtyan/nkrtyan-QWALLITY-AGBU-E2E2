from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging
import allure

class Helper:

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def _error_with_screenshot(self, message):
        logging.error(message)
        os.makedirs(self.test_logger.screenshot_dir, exist_ok=True)
        self.driver.save_screenshot(f"{self.test_logger.screenshot_dir}/{self.test_logger.test_name}.png")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=f"{self.test_logger.test_name}_failure",
            attachment_type=allure.attachment_type.PNG,
        )

    def navigate_to_page(self, url, new_window=False):
        try:
            if new_window:
                self.test_logger.info(f'Opening page in a new window: {url}')
                self.driver.execute_script(f"window.open('{url}'-1);") # поправлено под обычный open
            else:
                self.test_logger.info(f'Opening page: {url}')
                self.driver.get(url)
        except Exception as e:
            self._error_with_screenshot(f'Go to page failed: {e}')
            raise

    # Алиас для совместимости с тестами
    def go_to_page(self, url, new_window=False):
        self.navigate_to_page(url, new_window)

    def write_to_file(self, file_name, text):
        try:
            if file_name:
                with open(file_name, mode="a+", encoding="utf-8") as file:
                    file.write(f"{text}\n")
                self.test_logger.info(f'Appended text to file {file_name}: {text}')
        except Exception as e:
            self.test_logger.error(f'Append text to file failed for {file_name}: {e}')
            raise

    # Алиас для тестов
    def append_text_to_file(self, file_name, text):
        self.write_to_file(file_name, text)

    def get_and_accept_alert_text(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            self.test_logger.info(f'Accepted alert with text: {alert_text}')
            return alert_text
        except Exception as e:
            self._error_with_screenshot(f'Accept alert failed: {e}')
            raise

    # Алиас для тестов
    def accept_alert(self, timeout=5):
        return self.get_and_accept_alert_text(timeout)

    def scroll_to_element(self, by_locator): 
        try:
            element = self.driver.find_element(*by_locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.test_logger.info(f'Element scrolled to {by_locator} element')
        except Exception as e:
            self.test_logger.error(f'Scroll to element failed for {by_locator}: {e}')
            raise

    def wait_and_click(self, by_locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable(by_locator)
                    )
            element.click()
            self.test_logger.info(f'Clicked element: {by_locator}')
        except Exception as e:
            self._error_with_screenshot(f'Find and click failed for {by_locator}: {e}')
            raise

    # Алиас для тестов
    def find_and_click(self, by_locator, timeout=5):
        self.wait_and_click(by_locator, timeout)

    def wait_and_send_keys(self, by_locator, input_text, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            elem.send_keys(input_text)
            self.test_logger.info(f'Entered text into element: {by_locator}')
        except Exception as e:
            self._error_with_screenshot(f'Find and send keys failed for {by_locator}: {e}')
            raise

    def wait_and_get_attribute(self, by_locator, attribute, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            value = elem.get_attribute(attribute)
            self.test_logger.info(f'Got attribute {attribute} for element {by_locator}: {value}')
            return value
        except Exception as e:
            self._error_with_screenshot(f'Get attribute failed for {by_locator}: {e}')
            raise

    # Алиас для тестов
    def get_attribute(self, by_locator, attribute, timeout=5):
        return self.wait_and_get_attribute(by_locator, attribute, timeout)

    def wait_and_get_text(self, by_locator, timeout=5):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            text = elem.text
            self.test_logger.info(f'Got text for element {by_locator}: {text}')
            return text
        except Exception as e:
            self._error_with_screenshot(f'Get text failed for {by_locator}: {e}')
            raise

    # Алиас для тестов
    def get_text(self, by_locator, timeout=5):
        return self.wait_and_get_text(by_locator, timeout)

    def switch_window(self, window_id=0):
        try:
            self.driver.switch_to.window(self.driver.window_handles[window_id])
            self.test_logger.info(f'Switched to window: {window_id}')
        except Exception as e:
            self._error_with_screenshot(f'Switch window failed: {e}')
            raise