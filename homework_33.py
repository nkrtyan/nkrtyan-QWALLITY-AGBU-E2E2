import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test(driver):
    # TODO, here you should have checking regarding browser, which browser given, that driver is opening . Also add checking if the browser does not supported
    driver.get("https://python.org")
    driver.maximize_window()
    driver.implicitly_wait(5)
    
    search = driver.find_element(By.ID, "id-search-field")
    sent = driver.find_element(By.ID, "submit")
    
    search.send_keys("BlaBla")
    sent.click()
    
    time.sleep(5)
    
    information = driver.find_element(By.CLASS_NAME, "list-recent-events")
    
    if "No results found." in information.text:
        print("Everything is ok")
    else:
        print("Something went wrong")
        
    driver.quit()

# TODO, no need call the same function twice, you need to call it once and pass driver
test(webdriver.Chrome())
test(webdriver.Firefox())