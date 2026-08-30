import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browsers = ["chrome", "edge"]

for browser in browsers:
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()

    try:
        driver.maximize_window()

        driver.get("https://www.python.org")
        time.sleep(2)

        search_input = driver.find_element(By.ID, "id-search-field")
        go_button = driver.find_element(By.ID, "submit")

        search_input.send_keys("bla bla")
        go_button.click()

        time.sleep(3)

        result_element = driver.find_element(By.XPATH, "//p[contains(text(), 'No results found.')]")

        if result_element.is_displayed():
            print(f"[{browser}] SUCCESS: 'No results found.'")
        else:
            print(f"[{browser}] FAILED: Text is not displayed.")

        time.sleep(2)

    finally:
        driver.quit()