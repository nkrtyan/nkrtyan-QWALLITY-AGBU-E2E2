from selenium_test import webdriver
from selenium.webdriver.common.by import By

def find_elements(driver):
    elements = [
        driver.find_element(By.XPATH, "//input[@value='benz']"),
        driver.find_element(By.XPATH, "//*[contains(@class, 'checkbox')]"),
        driver.find_element(By.CSS_SELECTOR, "button[name='opentab']"),
        driver.find_element(By.CSS_SELECTOR, "select.multiple-select-example"),
        driver.find_element(By.XPATH, "//*[text()='Show Textbox']"),
        driver.find_element(By.CSS_SELECTOR, "input.displayed-text"),
        driver.find_element(By.XPATH, "//input[@name='enter-name']"),
        driver.find_element(By.XPATH, "//*[contains(text(), 'Mouse Hover Example')]"),
        driver.find_element(By.XPATH, "//td[contains(text(), 'Python Programming Language')]")
    ]
    return elements

def count_elements(elements):
    return len(elements)

def main():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.letskodeit.com/practice")

        elements = find_elements(driver)
        count = count_elements(elements)

        print(f"Total elements found: {count}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()