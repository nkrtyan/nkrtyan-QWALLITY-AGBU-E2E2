from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData import data

class ElementHelper:
    def scroll_to_element(self, browser, by_locator):
        element = browser.find_element(*by_locator)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def hover_element(self, browser, by_locator):
        element = self.scroll_to_element(browser, by_locator)
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        return element

    def wait_for_element_visible(self, browser, by_locator, timeout=20):
        return WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def wait_for_element_clickable(self, browser, by_locator, timeout=20):
            return WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )

class Helper:
    def browser(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        return browser

    def navigate_to_page(self, browser):
        browser.get(data.url)

    def close_browser(self, browser):
        if browser:
            browser.quit()

    def write_to_file(self, file_name, text, mode="a") -> None:
        with open(file_name, mode, encoding="utf-8") as file:
            file.write(f"{text}\n")

    def open_new_tab_and_switch(self, browser, url: str) -> None:
        browser.execute_script("window.open('');")
        new_tab = browser.window_handles[-1]
        browser.switch_to.window(new_tab)
        browser.get(url)

    def get_and_accept_alert_text(self, browser) -> str:
        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text