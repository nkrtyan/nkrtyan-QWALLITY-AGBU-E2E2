from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.letskodeit.com/practice")

elements = [
    (By.XPATH, "//input[@value='benz']"),
    (By.XPATH, "//input[@value='honda']"),
    (By.XPATH, "//a[contains(text(),'Open Tab')]"),
    (By.CSS_SELECTOR, "#multiple-select-example"),
    (By.CSS_SELECTOR, "#show-textbox"),
    (By.CSS_SELECTOR, "#displayed-text"),
    (By.XPATH, "//input[@id='name']"),
    (By.XPATH, "//input[@id='alertbtn']"),
    (By.XPATH, "//button[contains(text(),'Mouse Hover')]"),
    (By.CSS_SELECTOR, "table")
]

total = 0

for locator_type, locator in elements:
    found = driver.find_elements(locator_type, locator)
    total += len(found)

print("Total elements found:", total)

driver.quit()