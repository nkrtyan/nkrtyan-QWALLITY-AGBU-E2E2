from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browsers = [webdriver.Chrome, webdriver.Firefox]

def qa_testing(browser):
    driver = browser()
    driver.get("https://www.python.org/")
    search_field = driver.find_element(By.ID, "id-search-field")
    search_field.send_keys("BlaBlaBla")
    search_field.submit()
    time.sleep(4)
    page_text = driver.find_element(By.TAG_NAME, "body").text
    assert "No results found" in page_text
    print(f"{driver.name} test passed")
    driver.quit()
for browser in browsers:
    qa_testing(browser)
print("Success")