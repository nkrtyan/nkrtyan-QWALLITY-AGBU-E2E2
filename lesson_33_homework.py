from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browsers = ["chrome", "firefox"]

def test(driver):
    #FIXED, need to check here which broser, after open driver. Also add checking if unsuported browser, raise exception
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    try:
        driver.get("https://www.python.org/")

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

    except Exception as error:
        print(f"[{browser}] Test ERROR: {error}")

    
    driver.close()

# FIXED, add main block, and give list of browsers, based on for cycle pass driver to function, no need to repeat function call

if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")
        test(browser)