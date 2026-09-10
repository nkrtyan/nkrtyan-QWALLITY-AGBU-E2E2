from app.Helpers.logger import get_logger
logger = get_logger(__name__)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:
    """Generic utilities that don't belong to any single page: browser
    lifecycle management and writing results to the output text file."""

    def get_browser(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        return browser

    def navigate_to(self, browser, url):
        browser.get(url)

    def close_browser(self, browser):
        if browser:
            browser.quit()

    def write_to_file(self, filename, text, mode="a"):
        with open(filename, mode) as file:
            if mode == "a":
                file.write("\n")
            file.write(text)

    def open_new_tab_and_navigate(self, browser, url):
        # 12. Open a new tab, switch to the new tab
        original_handles = browser.window_handles
        browser.execute_script("window.open('')")
        WebDriverWait(browser, 10).until(EC.new_window_is_opened(original_handles))
        new_tab = browser.window_handles[-1]
        browser.switch_to.window(new_tab)
        # 13. Get google.com on the second tab
        browser.get(url)
