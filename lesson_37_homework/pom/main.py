from selenium.webdriver.common.by import By
from Helpers.lib import Helper

class LetsKodeitMainPage:
    open_alert = (By.ID, 'alertbtn')
    hide_btn = (By.ID, 'hide-textbox')
    element_locator = (By.ID, "displayed-text")
    hover_btn = (By.XPATH, '//button[@id="mousehover"]')
    top_btn = (By.XPATH, '//a[@href="#top"]')
    footer = (By.XPATH, "//p[contains(@class, 'jqCopyRight')]")

    def __init__(self, browser):
        self.browser = browser
        self.helper = Helper()

    def get_alert_text(self, file_name):
        self.browser.find_element(*self.open_alert).click()
        alert_text = self.helper.get_and_accept_alert_text(self.browser)
        # self.helper.write_to_file(file_name=file_name, text=alert_text, mode='a+') #FIXED move to get_and_accept_alert_text function
        return alert_text

    # def get_element_attribute(self, file_name):
    #     self.helper.wait_for_element_clickable(self.browser, self.hide_btn, action="click")
    #     style_value = self.helper.wait_for_element_visible(self.browser, self.element_locator, action="get_attribute",name="style")
    #     return style_value
        # self.helper.write_to_file(file_name=file_name, text=style_value, mode='a+') #TODO move to helper

    def get_element_attribute(self, file_name):
        # 1. Նախ գտնում ենք տեսանելի էլեմենտը և պահում element փոփոխականում
        element = self.helper.wait_for_element_visible(self.browser, self.element_locator)
        
        # 2. Սեղմում ենք Hide կոճակը
        self.helper.wait_for_element_clickable(self.browser, self.hide_btn, action="click")
        
        # 3. Քանի որ element օբյեկտը արդեն ձեռքի տակ ունենք, ուղղակի կանչում ենք get_attribute-ը
        style_value = element.get_attribute("style")
        
        return style_value
    def hover_and_click_top(self):
        self.helper.scroll_to_element(self.browser, self.hover_btn)
        # self.helper.hover_element(self.browser, self.hover_btn)
        top_elem = self.helper.wait_for_element_visible(self.browser, self.top_btn, action="click")
        

    def get_footer_text(self, file_name):
        footer_elem = self.helper.scroll_to_element(self.browser, self.footer) #TODO move to test case 
        return footer_elem.text
        # self.helper.write_to_file(file_name=file_name, text=footer_text, mode='a+')