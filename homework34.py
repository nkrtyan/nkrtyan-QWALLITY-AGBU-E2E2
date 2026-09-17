from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

# One CSS selector per highlighted element
selectors = [
    "#benzradio",  # Benz radio button
    "#hondacheck",  # Honda checkbox
    "#opentab",  # Open Tab button
    "option[value='peach']",  # Peach option
    "#show-textbox",  # Show button
    "#name",  # Enter Your Name field
    "div[id='mouse-hover-example-div'] div[class='left-align'] legend",  # Mouse Hover Example header
]

found_count = 0

for selector in selectors:
    if driver.find_elements(By.CSS_SELECTOR, selector):
        found_count = found_count + 1

print("Total elements found:", found_count)

driver.quit()