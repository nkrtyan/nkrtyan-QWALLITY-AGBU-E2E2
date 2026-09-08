from selenium import webdriver
from TestData import data
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementHelper:
    @staticmethod
    def scroll_to_element(browser, by_locator):
        """Գտնում է էլեմենտը և սքրոլ անում դեպի այն:"""
        element = browser.find_element(*by_locator)
        browser.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        return element

    @staticmethod
    def hover_element(browser, by_locator):
        """Սքրոլ է անում դեպի էլեմենտը և մկնիկը պահում վրան (hover):"""
        element = ElementHelper.scroll_to_element(browser, by_locator)
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        return element

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


    def write_to_file(file_name, text, mode) -> None:
        """
        Ֆայլում տեքստ ավելացնող/գրող helper ֆունկցիա:
        :param file_name: Ֆայլի անունը կամ ուղին (օր. 'live_coding_text.txt')
        :param text: Գրվող տեքստը
        :param mode: 'a' (append) - ավելացնել վերջից, 'w' (write) - վերագրել
        """
        with open(file_name, mode, encoding="utf-8") as file:
            file.write(f"{text}\n")


    def scroll_to_element(browser, by_locator):
        element = browser.find_element(*by_locator)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        return element


    def hover_element(browser, by_locator):
        element = ElementHelper.scroll_to_element(browser, by_locator)
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        return element

    def wait_for_element_visible(browser, by_locator, timeout=10):
        return WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def open_new_tab_and_switch(browser, url: str) -> None:

        browser.execute_script("window.open('');")
        new_tab = browser.window_handles[-1]  # Վերցնում է ամենավերջին բացված tab-ը
        browser.switch_to.window(new_tab)
        browser.get(url)