from app.Helpers.logger import get_logger
logger = get_logger(__name__)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime


class Helper:
   

    def get_browser(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        return browser

    def navigate_to(self, browser, url):
        browser.get(url)

    def close_browser(self, browser):
        if browser:
            browser.quit()

    def write_to_file(self, filename, text):
        with open(filename, "a+") as file:
            file.write(text)

    def open_new_tab_and_navigate(self, browser, url):
        # 12. Open a new tab, switch to the new tab
        original_handles = browser.window_handles
        browser.execute_script("window.open('')")
        WebDriverWait(browser, 10).until(EC.new_window_is_opened(original_handles))
        new_tab = browser.window_handles[1]
        browser.switch_to.window(new_tab)
        # 13. Get google.com on the second tab
        #browser.get(url)

    #def take_screenshot(self, browser, step_name, folder="screenshots"):+
        
       """ os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = os.path.join(folder, f"FAILED_{step_name}_{timestamp}.png")
        browser.save_screenshot(filename)
        logger.info(f"Screenshot saved: {filename}")
        return filename """
 
