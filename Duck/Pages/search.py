from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    search_input = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    def search(self, text):
        search_input = self.browser.find_element(*self.search_input)
        search_input.send_keys(text + Keys.ENTER)