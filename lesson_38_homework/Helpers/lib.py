from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_38_homework import config

class Helper:

    #TODO add __init__ for conftest methods, driver and logger 
    #TODO all functions put Try/except
    #TODO add logging for functions

    #TODO combine navigate_to_page and open_new_tab_and_switch functions
    def navigate_to_page(self, browser):
        browser.get(config.url)

    def open_new_tab_and_switch(self, browser, url):
        browser.execute_script("window.open('');")
        new_tab = browser.window_handles[0]
        browser.switch_to.window(new_tab)
        browser.get(config.new_tab_url)


    def write_to_file(self, file_name, text):
        if file_name:
            with open(file_name, mode="a+", encoding="utf-8") as file:
                file.write(f"{text}\n")

    def get_and_accept_alert_text(self, browser, file_name):
        alert = browser.switch_to.alert
        alert_text = alert.text
        self.write_to_file(file_name=file_name, text=alert_text) #TODO move to test scenar
        alert.accept()
        return alert_text

    def scroll_to_element(self, browser, by_locator): 
        element = browser.find_element(*by_locator)
        browser.execute_script("arguments[0].scrollIntoView();", element)


    def wait_for_element_visible(self, browser, by_locator, timeout=20): 
        element = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
       
        return element

    def wait_for_element_clickable(self, browser, by_locator, timeout=20): #TODO change function name
        element = WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
        element.click()

    #TODO add 4 functions, wait_and_click, wait_and_send_keys, wait_and_get_attribute, wait_and_get_text

    # def send_keys(self, browser, by_locator, text, timeout=20):
    #     element = self.wait_for_element_visible(browser, by_locator, timeout)
    #     element.clear()
    #     element.send_keys(text)
    #     return element
    

