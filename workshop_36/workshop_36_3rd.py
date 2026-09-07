"""Go to Text Input, enter any text, click the button and check if the button text is the same as the
entered text."""

from selenium import webdriver
from selenium.webdriver.common.by import By


my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("http://www.uitestingplayground.com/")
text_input = my_driver.find_element(By.XPATH, '//a[text()="Text Input"]')
text_input.click()
input_locator = my_driver.find_element(By.XPATH, '//input[@placeholder = "MyButton"]')
input_locator.send_keys("BlaBla")
main_button = my_driver.find_element(By.XPATH, '//button[@id = "updatingButton"]')
main_button.click()

def check_button_name():
    if main_button.text == input_locator.get_attribute("value"):
        print("button name changed")

    else:
        print("Error. Botton namen haven't changed")


if __name__=="__main__":
    check_button_name()