"""   Lesson_33: Selenium Webdriver

Create program, which open Chrome driver
Navigate python.org
Enter "BlaBla"
Check that "No found result" text displays
Close driver
IMPORTANT: The code should work for two different browsers automatically.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def call_test(my_driver):
    my_driver.maximize_window()

    my_driver.get("https://www.python.org/")

    search = my_driver.find_element(By.NAME, "q")
    submit = my_driver.find_element(By.NAME, "submit")
    time.sleep(2)
    search.send_keys("BlaBla")
    time.sleep(2)
    submit.click()
    time.sleep(2)
    print(my_driver.current_url)


    result = my_driver.find_element(
        By.XPATH,
        "//*[contains(text(), 'No results found')]"
    )

    assert result.is_displayed()

    print("Test PASSED")

    my_driver.close()

call_test(webdriver.Chrome())
call_test(webdriver.Firefox())
