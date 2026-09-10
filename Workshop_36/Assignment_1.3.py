from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_text_input():
    # Chrome settings for Privacy Error
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
    
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver.get("https://www.uitestingplayground.com/textinput")

       

        text = "Kristine"

        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.send_keys(text)

        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        assert button.text == text

        print("Test passed!")

        driver.quit()


if __name__ == "__main__":
    test_text_input()