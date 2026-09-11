from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData import data, config

class Helper:
    def browser(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        return browser

    def navigate_to_page(self, browser):
        browser.get(config.url)


    def write_to_file(self, file_name, text, mode="a"):
        with open(file_name, mode=mode, encoding="utf-8") as file:
            file.write(f"{text}\n")

    def get_and_accept_alert_text(self, browser, file_name):
        alert = browser.switch_to.alert
        alert_text = alert.text
        self.helper.write_to_file(file_name=file_name, text=alert_text)
        alert.accept()
        return alert_text

    def scroll_to_element(self, browser, by_locator): 
        element = browser.find_element(*by_locator)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        return element

    # def hover_element(self, browser, by_locator): #FIXED connect scroll_to_element and hover_element 
    #     element = self.scroll_to_element(browser, by_locator)
    #     actions = ActionChains(browser)
    #     actions.move_to_element(element).perform()
    #     return element

    def wait_for_element_visible(self, browser, by_locator, timeout=20, action=None, *args, **kwargs): #FIXED add atribute for actions(click, sned_keys, etc)
        element = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

        if action:
            method = getattr(element, action)  # Գտնում է element.click, element.send_keys և այլն
            return method(*args, **kwargs)     # Կանչում է մեթոդը՝ փոխանցելով բոլոր արգումենտները
                    

        # if action == "click":
        #     element.click()
        # elif action == "send_keys" and value is not None:
        #     element.send_keys(value)
        # elif action == "clear":
        #     element.clear()
            
        return element

    def wait_for_element_clickable(self, browser, by_locator, timeout=20, action=None, *args, **kwargs):
        element = WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
        
        if action:
            method = getattr(element, action)  # Գտնում է element.click, element.send_keys և այլն
            return method(*args, **kwargs)     # Կանչում է մեթոդը՝ փոխանցելով բոլոր արգումենտները
            
        return element

    def open_new_tab_and_switch(self, browser, url):
        browser.execute_script("window.open('');")
        new_tab = browser.window_handles[-1]
        browser.switch_to.window(new_tab)
        browser.get(config.new_tab_url)


#FIXED add 2 functions wait_and_click, wait_and_send_keys
#TODO add loggiing in functions
#FIXED create config file add environment 