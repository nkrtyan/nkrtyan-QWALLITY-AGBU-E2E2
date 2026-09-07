from selenium_test import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

def find_element(driver):
   
    search_field = driver.find_element(By.XPATH, "//input[@name='q']")
    search_field.send_keys("Selenium")
    search_field.clear()
    search_field.send_keys("Python")
    time.sleep(10)

find_element(driver)

driver.quit
