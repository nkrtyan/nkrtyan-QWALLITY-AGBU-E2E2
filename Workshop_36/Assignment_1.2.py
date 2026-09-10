from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_progress_bar():

    # Chrome settings for Privacy Error
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://www.uitestingplayground.com/progressbar")

    wait = WebDriverWait(driver, 10)

    # Start button
    start_button = wait.until(
        EC.element_to_be_clickable((By.ID, "startButton"))
    )
    start_button.click()

    # Let the progress bar run
    time.sleep(2)

    # Stop button
    stop_button = wait.until(
        EC.element_to_be_clickable((By.ID, "stopButton"))
    )
    stop_button.click()

    # Get result
    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    print(result)

    # Get Duration
    duration = result.split("duration: ")[1]

    print("Duration:", duration)

    driver.quit()


if __name__ == "__main__":
    test_progress_bar()