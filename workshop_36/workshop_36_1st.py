""". Go to Visibility, click the Hide button. Check in your program that buttons are hidden.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("http://www.uitestingplayground.com/")
visibility_lokator = my_driver.find_element(By.XPATH, '//a[text()="Visibility"]')
visibility_lokator.click()

removed_btn =(By.XPATH, '//button[text()="Removed"]')
zero_btn = (By.XPATH, '//button[text() = "Zero Width"]')
overlapped_btn =(By.XPATH, '//button[text() = "Overlapped"]')
opacity_button = (By.XPATH, '//*[@id="transparentButton"]')
visibiltyhidden_button = (By.XPATH, '//*[@id="invisibleButton"]')
displaynone_button = (By.XPATH, '//*[@id="invisibleButton"]')
offscreen_button = (By.XPATH, '//*[@id="offscreenButton"]')



btn_list = [removed_btn, zero_btn, overlapped_btn, opacity_button, visibiltyhidden_button, displaynone_button, offscreen_button]

hide_button = my_driver.find_element(By.XPATH, '//button[text()="Hide"]')
hide_button.click()

def check_list(btn_list):
    for i in btn_list:
        try:
            if i==overlapped_btn:
                if my_driver.find_element(By.XPATH, '//div[@style="position: absolute; background-color: white; width: 108px; height: 38px; left: 1231.25px; top: 487.188px;"]').is_enabled():
                    print(f"{i} is hidden")

                else:
                    print(f"{i} is not hidden")

            elif not my_driver.find_element(*i).is_displayed():
                print(f"{i} is hidden")

            else:
                print(f"{i} is not hidden")

        except:
            print(f"{i} button is hidden")





if __name__=="__main__":
    check_list(btn_list)