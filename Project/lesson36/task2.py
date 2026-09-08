from selenium import webdriver
from selenium.webdriver.common.by import By
import time


my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("http://www.uitestingplayground.com/")
progres_bar = my_driver.find_element(By.XPATH, '//a[text()="Progress Bar"]')
progres_bar.click()
start_btn = my_driver.find_element(By.XPATH, '//button[text()="Start"]') 
start_btn.click()
time.sleep(2)
stop_btn = my_driver.find_element(By.XPATH, '//button[text()="Stop                "]')
stop_btn.click()
duration = my_driver.find_element(By.XPATH, '//p[@id="result"]').text


print(duration.split("duration: ")[1])

