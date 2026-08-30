from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test(driver):
    driver.get("https://www.python.org/")
    driver.maximize_window()

    search = driver.find_element(By.ID, "id-search-field")
    sent = driver.find_element(By.ID, "submit")

    search.send_keys("BlaBla")
    sent.click()

    time.sleep(8)

    information = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul')

    if information.text == "No results found.":
        print("Automation test passed")
    else:
        print("Automation test failed")
    
    driver.close()

test(webdriver.Chrome())