from selenium import webdriver
from selenium.webdriver.common.by import By


def find_elements(driver):
    elements = [
        driver.find_element(By.XPATH, "//input[@value='benz']"),
        driver.find_element(By.ID, "hondacheck"),
        driver.find_element(By.ID, "opentab"),
        driver.find_element(By.ID, "multiple-select-example"),
        driver.find_element(By.ID, "show-textbox"),
        driver.find_element(By.ID, "displayed-text"),
        driver.find_element(By.ID, "name"),
        driver.find_element(By.XPATH, "//*[text()='Mouse Hover Example']"),
        driver.find_element(By.XPATH, "//td[text()='Python Programming Language']")
    ]

    return elements


def count_elements(elements):
    return len(elements)


driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
elements = find_elements(driver)
count = count_elements(elements)
print("Total elements found:", count)

driver.quit()