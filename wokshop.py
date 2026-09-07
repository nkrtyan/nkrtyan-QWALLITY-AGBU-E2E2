from selenium_test import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.uitestingplayground.com/")

visibility = driver.find_element(By.XPATH, "//a[@href='/visibility']")
visibility.click()

hide = driver.find_element(By.ID, "hideButton")
# hide.click()

# btn = driver.find_element (By.XPATH,"//button[@type='button' and @id='removedButton']").is_displayed()

# print(btn)

# driver.quit()
zero_width = driver.find_element(By.XPATH, "//button[@type='button' and @id = 'zeroWidthButton']").get_attribute("btn btn-warning zerowidth")
print(zero_width)

overlapped = driver.find_element(By.XPATH, "//button[@type='button' and @id = 'overlappedButton']").get_attribute("background-color: white")
print(overlapped)

opacity = driver.find_element(By.XPATH, "//button[@type = 'button' and @id = 'transparentButton']").get_attribute("opacity: 0")
print(opacity)

visibility_hidden = driver.find_element(By.XPATH, "//button[@type = 'button'and @id='invisibleButton']").get_attribute("visibility: hidden")
print(visibility_hidden)

display_none = driver.find_element(By.XPATH, "//button[@type='button' and @id='notdisplayedButton']").get_attribute("display: none;")
print(display_none)

offscreen = driver.find_element(By.XPATH, "//button[@type='button' and @id='offscreenButton']").get_attribute("btn btn-info offscreen")
print(offscreen)