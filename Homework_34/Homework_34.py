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





from selenium import webdriver
from selenium.webdriver.common.by import By


def find_highlighted_elements(driver):
    """
    Find all elements highlighted in the assignment.
    Return the total number of elements found.
    """

    selectors = [
        # 1. Benz Radio Button
        (
            "Benz Radio Button",
            By.CSS_SELECTOR,
            "#benzradio"
        ),

        # 2. Honda Checkbox
        (
            "Honda Checkbox",
            By.CSS_SELECTOR,
            "#hondacheck"
        ),

        # 3. Open Tab
        (
            "Open Tab",
            By.CSS_SELECTOR,
            "#opentab"
        ),

        # 4. Orange option
        (
            "Orange",
            By.CSS_SELECTOR,
            "#multiple-select-example option[value='orange']"
        ),

        # 5. Peach option
        (
            "Peach",
            By.CSS_SELECTOR,
            "#multiple-select-example option[value='peach']"
        ),

        # 6. Show button
        (
            "Show Button",
            By.CSS_SELECTOR,
            "#show-textbox"
        ),

        # 7. Hide/Show textbox
        (
            "Hide/Show Textbox",
            By.CSS_SELECTOR,
            "#displayed-text"
        ),

        # 8. Enter Your Name
        (
    "Enter Your Name",
    By.CSS_SELECTOR,
    "input[placeholder='Enter Your Name']"
),

        # 9. Mouse Hover Example button
        (
            "Mouse Hover Button",
            By.CSS_SELECTOR,
            "#mousehover"
        )
    ]

    total = 0

    for name, locator_type, locator in selectors:

        elements = driver.find_elements(locator_type, locator)

        print(f"{name}: {len(elements)}")

        total += len(elements)

    return total


def main():

    # Create Chrome browser
    driver = webdriver.Chrome()

    try:
        # Open Practice Page
        driver.get("https://www.letskodeit.com/practice")

        # Maximize browser
        driver.maximize_window()

        # Find highlighted elements
        total = find_highlighted_elements(driver)

        # Print total number
        print("----------------------------")
        print(f"Total elements found: {total}")
        print("----------------------------")

    finally:
        # Close browser
        driver.quit()


if __name__ == "__main__":
    main()