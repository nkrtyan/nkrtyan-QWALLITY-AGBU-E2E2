from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    link_divs = (By.XPATH, "//a[@data-testid='result-title-a']")
    search_input = (By.XPATH, "//textarea[@name='q']")

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.link_divs)
        return len(link_divs)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.search_input)
        return search_input.get_attribute('value')

    def get_link_divs(self):
        link_text = []
        search_input = self.browser.find_elements(*self.link_divs)
        link_texts = [link.text for link in search_input]
        for i in search_input:
            if text in i.text:
                pass
            else:
                logging.error(i.text)
                save.screen
            
            link_text.append(i.text)
            print(i.text)
        return link_texts