from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from workshop_37.assignement_ind import test_data
from workshop_37.assignement_ind.helpers import Helper
from workshop_37.assignement_ind.pom.main_page import Letskodeit_main_page


# 9. Click on the Sign In button
# 10. Fill the fields with incorrect email or password and click the LogIn button
# 11. Get validation message and write in the txt file

class Sign_in(Letskodeit_main_page):
    sign_in_btn = (By.XPATH, '//a[contains(text(), "Sign In")]')
    username_field = (By.XPATH, '//input[@name="email"]')
    password_field = (By.XPATH, '//input[@name="password"]')
    login_btn = (By.XPATH, '//button[@id="login"]')
    validation_message = (By.XPATH, '//span[text()="The email must be a valid email address."]')


    def __init__(self, my_driver, username, password):
        super().__init__(my_driver)
        self.username = username
        self.password = password


    def sign_in(self): 
        sign_in_btn = self.my_driver.find_element(*self.sign_in_btn)
        sign_in_btn.click()

        username_field = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.username_field))
        # self.my_driver.find_element(*self.username_field)
        username_field.click()
        username_field.send_keys(self.username)

        password_field = WebDriverWait(self.my_driver, 10).umtil(EC.visibility_of_element_located(self.password_field))
        password_field.click()
        password_field.send_keys(self.password)

        login_btn = WebDriverWait(self.my_driver, 10). until(EC.element_to_be_clickable(self.login_btn))
        login_btn.click()

        validation_message = WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located(self.validation_message))

        self.helper.open_file("\n" + validation_message.text, "a") 


# 12. Open a new tab, switch to the new tab
# 13. Get google.com on the second tab


    def open_other_tab(self):

        self.my_driver.execute_script("window.open('')")

        new_tab = self.my_driver.window_handles[1]
        self.my_driver.switch_to.window(new_tab)
        self.my_driver.implicitly_wait(10)

        self.my_driver.get("https://www.google.com")
        self.my_driver.implicitly_wait(10)

        print(self.my_driver.current_url)
