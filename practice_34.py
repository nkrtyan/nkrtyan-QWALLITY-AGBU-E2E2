from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()


xpaths = {
    
    "Radio Section (Class + Child)": (
        "//div[@class='left-align']//label[@for='benz']"
    ),
    
    "Radio Legend (Direct Child)": "//fieldset/legend",
    
    "Checkbox Section (Class)": "//div[contains(@class, 'cen-align')]",
    
    "Select Dropdown (Direct Child)": (
        "//div[@id='select-class-example']/select"
    ),
    
    "Web Table Cell (Child)": (
        "//table[@id='product']//td[contains(text(), 'Python Programming"
        " Language')]"
    ),
    
    "Multiple Select": "//select[@id='multiple-select-example']",
    "Displayed Text Field": "//input[@id='displayed-text']",
    "Mouse Hover Button": "//button[@id='mousehover']",
    "Open Window Button": "//button[@id='openwindow']",
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