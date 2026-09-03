from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

xpaths = {
    "Radio Button (Benz)": "//fieldset[legend='Radio Button Example']//input[@id='benzradio']",
    "Checkbox (Benz)": "//fieldset[legend='Checkbox Example']//input[@id='benzcheck']",
    "Select Car Dropdown": "//div[@id='select-class-example']//select[@id='carselect']",
    "Multiple Select": "//select[@id='multiple-select-example']",
    "Displayed Text Field": "//input[@id='displayed-text']",
    "Mouse Hover Button": "//button[@id='mousehover']",
    "Open Window Button": "//button[@id='openwindow']",
    "Open Tab Link": "//a[@id='opentab']",
    "Web Table Cell": "//table[@id='product']/tbody/tr/td[contains(text(), 'Python Programming Language')]"
}

total_count = 0

for name, xpath in xpaths.items():
    elements = driver.find_elements(By.XPATH, xpath)
    count = len(elements)
    total_count += count
    
    if count > 0:
        print(f"{name}: {count} element(s) found.")
    else:
        print(f"{name}: 0 elements found.")

print(f"\nTotal elements found across all selectors: {total_count}")