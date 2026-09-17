from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
 
browsers = ["chrome", "firefox"]
 
def negative_search_test(browser_name, search_term="blabla"):
    """Open python.org on the given browser, search for a term that
    should return no results, and check that 'No results found.' is shown."""
 
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
 
    driver.maximize_window()
 
    try:
        driver.get("https://www.python.org/")
        time.sleep(2)  # wait for homepage to load
 
        search_box = driver.find_element(By.ID, "id-search-field")
        search_box.send_keys(search_term)
        time.sleep(1)
 
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(4)  # wait for results page to load
 
        results_section = driver.find_element(By.CLASS_NAME, "list-recent-events")
        results_text = results_section.text
        print(f"[{browser_name}] Results section says: {results_text!r}")
 
        if "No results found." in results_text:
            print(f"[{browser_name}] Test PASSED")
        else:
            print(f"[{browser_name}] Test FAILED")
 
    except Exception as error:
        print(f"[{browser_name}] Test ERROR: {error}")
 
    finally:
        driver.quit()
 
 
for browser_name in browsers:
    negative_search_test(browser_name)

#  great job, no comments :)
 