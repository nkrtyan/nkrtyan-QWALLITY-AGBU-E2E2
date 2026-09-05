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

        progress_bar = driver.find_element(By.XPATH, '//a[@href="/progressbar"]')
        
        progress_bar.click()

        start_btn = driver.find_element(By.ID, "startButton")
        stop_btn = driver.find_element(By.ID, "stopButton")
        result = driver.find_element(By.ID, "result")

        return start_btn, stop_btn, result

    except Exception as error:
            print(f"[{browser}] Test ERROR: {error}")
    
def test(start_btn, stop_btn, result):


    start_btn.click()

    time.sleep(5)

    stop_btn.click()

    text = result.text

    duration = text.split("duration:")[1].strip()

    print(f"Duration: {duration}")


if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")

        elements = get_elements(browser)
        test(*elements)
