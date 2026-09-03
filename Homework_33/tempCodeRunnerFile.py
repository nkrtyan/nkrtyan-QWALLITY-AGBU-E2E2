from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_search(browser_name):

    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()

    driver.get("https://www.python.org/")

    search_field = driver.find_element(By.ID, "id-search-field")
    search_field.send_keys("BlaBla")
    search_field.submit()

    time.sleep(6)

    page_text = driver.find_element(By.TAG_NAME, "body").text

    assert "No results found" in page_text

    print(f"{browser_name} test passed")

    driver.close()


def main():

    test_search("chrome")
    test_search("edge")


if __name__ == "__main__":
    main()