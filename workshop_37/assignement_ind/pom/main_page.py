from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from workshop_37.assignement_ind import test_data
from workshop_37.assignement_ind.helpers import Helper
import logging


# 3. Click to open the Alert popup
# 4. Get text from the popup
# 5. Open txt file with live_coding_text.txt file name and write there popup text

class Letskodeit_main_page:
    alert_btn = (By.XPATH, '//input[@id = "alertbtn"]')
    hide_show_element = (By.XPATH, '//input[@id = "displayed-text"]')
    hide_btn = (By.XPATH, '//input[@id = "hide-textbox"]')
    changed_attribute = (By.XPATH, '//input[starts-with(@style, "display:")]')
    mouse_hove_btn = (By.XPATH, '//button[@id = "mousehover"]')
    mouse_btn_top = (By.XPATH, '//a[text()= "Top"]')
    scroll_footer = (By.XPATH, "/html/body/div[1]/div[3]/div/span/div/div[1]/div/div[1]/p")

    def __init__(self, my_driver):
        self.my_driver = my_driver
        self.helper = Helper()


    def alert_click(self):

        try:
            alert_btn_click = self.my_driver.find_element(*self.alert_btn)
            alert_btn_click.click()

            popup = self.my_driver.switch_to.alert
            self.helper.open_file(popup.text)

            popup.accept()

        except Exception as e:
            logging.error("Error while handling alert: %s", e)



# 6. Locate the mentioned element, hide it, and then add the attribute and its value, based on which it shows and hides, to the text file
    def hide_show_function(self):
        hide_show_element = self.my_driver.find_element(*self.hide_show_element)
        hide_show_element.click()

        hide_btn = self.my_driver.find_element(*self.hide_btn)
        hide_btn.click()

        changed_attribute = self.my_driver.find_element(*self.changed_attribute)

        style = changed_attribute.get_attribute("style")
  
        self.helper.open_file("\n" + style, "a")

# 7. Move to Mouse Hover button, click on it and Click on Top option to go to the top of screen
    def mouse_hover(self):
        mouse_hove_btn = self.my_driver.find_element(*self.mouse_hove_btn)
        mouse_hove_btn.click()

        time.sleep(2)

        mouse_btn_top = self.my_driver.find_element(*self.mouse_btn_top)
        actions = ActionChains(self.my_driver)
        actions.move_to_element(mouse_btn_top).perform()

# 8. Move to the footer and write text in the opened file

    def scroll_function(self):
        scroll_footer = self.my_driver.find_element(*self.scroll_footer)
        self.my_driver.execute_script(
            "arguments[0].scrollIntoView();",
            scroll_footer)
        time.sleep(2)
        with open("live_coding_text.txt", "a") as file:
            file.write("\n")
            file.write(scroll_footer.text)