import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")
time.sleep(3)

elements_to_find = {
    "Radio Button (BMW)": "input#bmwradio",
    "Checkbox (Benz)": "input#benzcheck",
    "Open Window Button": "button#openwindow",
    "Open Tab Button": "a#opentab",
    "Car Dropdown Select": "select#carselect",
    "Multiple Select (Orange/Apple)": "select#multiple-select-example",
    "Hide/Show Textbox Field": "input#displayed-text",
    "Hide Button": "input#hide-textbox",
    "Show Button": "input#show-textbox",
    "Enter Your Name Field": "input[name='enter-name']",
    "Alert Button": "input#alertbtn",
    "Confirm Button": "input#confirmbtn",
    "Mouse Hover Button": "button#mousehover",
    "Web Table Element": "table#product"
}

found_count = 0
print("🔍 Starting element testing...\n")

for name, css_selector in elements_to_find.items():
    try:
        element = driver.find_element(By.CSS_SELECTOR, css_selector)
        if name == "Radio Button (BMW)" or name == "Checkbox (Benz)":
            element.click()
        elif name == "Enter Your Name Field":
            element.send_keys("QA Tester")
        print(f"✅ Successfully found -> {name} (CSS: {css_selector})")
        found_count += 1
    except Exception as e:
        print(f"❌ Failed to find element -> {name}")

print("\n==================================================")
print(f"📊 TOTAL ELEMENTS FOUND: {found_count} / {len(elements_to_find)}")
print("==================================================")

time.sleep(4)
driver.quit()
