from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")

time.sleep(5)



locators = [
    [By.CSS_SELECTOR, "div#radio-btn-example label[for='benz']"],
    [By.CSS_SELECTOR, "div#checkbox-example-div label[for='honda']"],
    [By.CSS_SELECTOR, "div#open-tab-example-div a#opentab"],
    [By.CSS_SELECTOR, "#multiple-select-example option[value='orange']"],
    [By.CSS_SELECTOR, "#multiple-select-example option[value='peach']"],
    [By.CSS_SELECTOR, "div#hide-show-example-div input[value='Show']"],
    [By.CSS_SELECTOR, "div#alert-example-div input#name"],
    [By.CSS_SELECTOR, "div#hide-show-example-div input#displayed-text"],
    [By.CSS_SELECTOR, "div#mouse-hover-example-div"],
    [By.XPATH, "//table[@id='product']//td[text()='Python Programming Language']"]
]



total_found = 0



for loc in locators:
    elements = driver.find_elements(*loc)
  #driver.find_elements(By.CSS_SELECTOR, "benz")
    total_found += len(elements)



print(f"All element's count is {total_found}")



driver.close()