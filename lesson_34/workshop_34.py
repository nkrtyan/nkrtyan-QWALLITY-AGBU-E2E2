"""Assignments 
1. Navigate by the following URL:  https://www.letskodeit.com/practice
2. Find effective XPaths/CSS selector  for the elements that are highlighted in the screenshot below.
3. Print how many elements you found in total.

"""

"""Locators

benz = my_driver.find_element(By.XPATH, "//input[contains(@id, 'benzradio')]/ancestor::label")
honda = my_driver.find_element(By.XPATH, "//input[@id='hondacheck']/ancestor::label")
open_tab= my_driver.find_element(By.CSS_SELECTOR, "a#opentab")
select_orange = my_driver.find_element(By.CSS_SELECTOR, "select option[value='orange']")
select_peach = my_driver.find_element(By.CSS_SELECTOR, 'select option[value="peach"]')
show = my_driver.find_element(By.CSS_SELECTOR, "input#show-textbox")
hide_show_example = my_driver.find_element(By.CSS_SELECTOR, "input#displayed-text")
enter_name = my_driver.find_element(By.CSS_SELECTOR, "fieldset>input[name='enter-name']")
mouse_hover = my_driver.find_element(By.XPATH, '//*[text()="Mouse Hover Example"]')
course = my_driver.find_element(By.CSS_SELECTOR, 'tr:nth-of-type(3) td.course-name')

"""

from selenium import webdriver
from selenium.webdriver.common.by import By


my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("https://www.letskodeit.com/practice")



def find_element_and_count(by, locator):
    global count
    try: 
        my_driver.find_element(by, locator)
        count += 1
        

    except:
        print(f"LOCATOR '{locator}' not found")
        

    return count

count=0

find_element_and_count(By.XPATH, "//input[contains(@id, 'benzradio')]/ancestor::label")
find_element_and_count(By.XPATH, "//input[@id='hondacheck']/ancestor::labe") #False locator for example
find_element_and_count(By.XPATH, "//input[@id='hondacheck']/ancestor::label")
find_element_and_count(By.CSS_SELECTOR, "a#opentab")
find_element_and_count(By.CSS_SELECTOR, "select option[value='orange']")
find_element_and_count(By.CSS_SELECTOR, 'select option[value="peach"]')
find_element_and_count(By.CSS_SELECTOR, "input#show-textbox")
find_element_and_count(By.CSS_SELECTOR, "input#displayed-text")
find_element_and_count(By.CSS_SELECTOR, "fieldset>input[name='enter-name'")
find_element_and_count(By.XPATH, '//*[text()="Mouse Hover Example"]')
find_element_and_count(By.CSS_SELECTOR, 'tr:nth-of-type(3) td.course-name')


print("Total find elements", count)