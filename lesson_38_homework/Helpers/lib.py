from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData import config

class Helper:

    def navigate_to_page(self, browser):
        browser.get(config.url)

    def write_to_file(self, file_name, text, mode="a"):
        if file_name:
            with open(file_name, mode=mode, encoding="utf-8") as file:
                file.write(f"{text}\n")

    def get_and_accept_alert_text(self, browser, file_name):
        alert = browser.switch_to.alert
        alert_text = alert.text
        self.write_to_file(file_name=file_name, text=alert_text)
        alert.accept()
        return alert_text

    def scroll_to_element(self, browser, by_locator): 
        element = browser.find_element(*by_locator)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        return element


    def wait_for_element_visible(self, browser, by_locator, timeout=20): 
        element = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
       
        return element

    def wait_for_element_clickable(self, browser, by_locator, timeout=20):
        element = WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
        element.click()

        return element
    
    def send_keys(self, browser, by_locator, text, timeout=20):
        element = self.wait_for_element_visible(browser, by_locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
    
    def open_new_tab_and_switch(self, browser, url):
        browser.execute_script("window.open('');")
        new_tab = browser.window_handles[0]
        browser.switch_to.window(new_tab)
        browser.get(config.new_tab_url)

