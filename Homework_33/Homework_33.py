from selenium import webdriver # practise
import time

# TODO,  this should be moved under function and pass browser name as an argument
my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("https://www.python.org/")
time.sleep(6)
print(my_driver.title)
print(my_driver.current_url)
my_driver.close()
print("success")




# TODO, no need keep few options, solve in one option,  move all imports at the above
from selenium import webdriver # Option 1
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

search_field = driver.find_element(By.ID, "id-search-field")
search_field.send_keys("BlaBla")

search_field.submit()

result = driver.find_element(By.TAG_NAME, "body").text

assert "No results found" in result

print("Test passed: 'No results found' text is displayed.")

driver.quit()






from selenium import webdriver # Option 2
from selenium.webdriver.common.by import By
import time


browsers = [
    webdriver.Chrome(),
    webdriver.Edge()
]

for driver in browsers:

    driver.maximize_window()

    driver.get("https://www.python.org/")

    search_field = driver.find_element(By.ID, "id-search-field")
    search_field.send_keys("BlaBla")
    search_field.submit()

    time.sleep(6)

    page_text = driver.find_element(By.TAG_NAME, "body").text

    assert "No results found" in page_text

    print(f"{driver.name} test passed")

    driver.close()

print("Success")

# TODO, i dont see main block, where you should call you function with logic. that function should get browser name 
# TODO, in case if the browser does not support, you will get error, so need to develop