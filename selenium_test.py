from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browsers = [webdriver.Chrome, webdriver.Firefox]
def qa_testing(browser):
    driver = browser()

    try:
        driver.get("https://www.python.org/")

        search_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id-search-field"))
        )

        search_field.send_keys("BlaBlaBla")
        search_field.submit()

        page_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        ).text

        assert "No results found" in page_text

        print(f"{driver.name} test passed")

    finally:
        driver.quit()

if __name__ == "__main__":
    for browser in browsers:
        qa_testing(browser)

    print("Success")