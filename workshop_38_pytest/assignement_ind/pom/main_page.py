from selenium.webdriver.common.by import By
from workshop_38_pytest.assignement_ind.helpers import Helper



# 3. Click to open the Alert popup
# 4. Get text from the popup
# 5. Open txt file with live_coding_text.txt file name and write there popup text

class Letskodeit_main_page(Helper):
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

# username_field = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.username_field))

    def alert_click(self):

        try:
            alert_btn_click = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.alert_btn))
            alert_btn_click.click()

            popup = self.my_driver.switch_to.alert
            self.helper.open_file(popup.text)

            popup.accept()

            logging.info("Alert action completed")
            

        except Exception as e:
            logging.error("Error while handling alert: %s", e)
            raise



# 6. Locate the mentioned element, hide it, and then add the attribute and its value, based on which it shows and hides, to the text file
    def hide_show_function(self):
        try:
        
            hide_show_element = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.hide_show_element))
            hide_show_element.click()

            hide_btn = self.my_driver.find_element(*self.hide_btn)
            hide_btn.click()

            changed_attribute = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.changed_attribute))

            style = changed_attribute.get_attribute("style")
    
            self.helper.open_file("\n" + style, "a")

            logging.info("Hide/Show action completed")

        except Exception as e:
            logging.error("Error while handling Hide/Show action: %s", e)

# 7. Move to Mouse Hover button, click on it and Click on Top option to go to the top of screen
    def mouse_hover(self):
        try:
            mouse_hove_btn = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.mouse_hove_btn))
            mouse_hove_btn.click()
            mouse_btn_top = WebDriverWait(self.my_driver, 10). until(EC.visibility_of_element_located(self.mouse_btn_top))
            actions = ActionChains(self.my_driver)
            actions.move_to_element(mouse_btn_top).perform()

            logging.info("Mouse hover action completed")

        except Exception as e:
            logging.error("Error while handling mouse hover action: %s", e)
        

# 8. Move to the footer and write text in the opened file

    def scroll_function(self):
        try:
            scroll_footer = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.scroll_footer))
            self.my_driver.execute_script(
                "arguments[0].scrollIntoView();",
                scroll_footer)
            self.helper.open_file("\n" + scroll_footer.text, "a")
            logging.info("Scroll function action completed")

        except Exception as e:
            logging.error("Error while handling Scroll function action: %s", e)
