from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test(driver):
    # TODO, need to check here which broser, after open driver. Also add checking if unsuported browser, raise exception
    driver.get("https://www.python.org/")
    driver.maximize_window()

    search = driver.find_element(By.ID, "id-search-field")
    sent = driver.find_element(By.ID, "submit")

    search.send_keys("BlaBla")
    sent.click()

    time.sleep(3)

    information = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul')

    if information.text == "No results found.":
        print("Everything is ok")
    else:
        print("Something went wrong")
    
    driver.close()

# TODO, add main block, and give list of browsers, based on for cycle pass driver to function, no need to repeat function call
test(webdriver.Chrome())
test(webdriver.Firefox())