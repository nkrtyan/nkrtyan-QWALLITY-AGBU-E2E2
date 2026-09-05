from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browsers = ["Chrome"]


def get_elements(browser):

    if browser == "Chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    try:

        driver.get("http://www.uitestingplayground.com/")

        input_txt = driver.find_element(By.XPATH, '//a[@href="/textinput"]')
        
        input_txt.click()

        inp_txt = driver.find_element(By.ID, "newButtonName").send_keys("blabla")
        btn = driver.find_element(By.CSS_SELECTOR, "button#updatingButton").click()
        btn_after_click = driver.find_element(By.XPATH, '//button[text()="blabla"]').text
        if btn_after_click == "blabla":
            print(True)

    except Exception as error:
            print(f"[{browser}] Test ERROR: {error}")
    

if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")

        elements = get_elements(browser)
