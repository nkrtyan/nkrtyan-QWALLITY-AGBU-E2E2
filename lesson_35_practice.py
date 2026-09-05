# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# driver = webdriver.Chrome()
# # driver.get("https://www.python.org/")
# driver.get("https://www.letskodeit.com/practice")
# driver.maximize_window()
# driver.set_page_load_timeout(60)

# element_text = driver.find_element(By.CLASS_NAME, "donate-button").get_attribute("href")
# print(element_text)

# element = driver.find_element(By.NAME, "q")
# element.send_keys("Bla bla")
# driver.find_element(By.ID, "submit").click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# driver.refresh()
# print(driver.current_url)
# print(driver.title)
# element_donate = driver.find_element(By.CLASS_NAME, "donate-button").is_displayed()
# print(element_donate)
# driver.close()

# --------------
# select_element = Select(driver.find_element(By.ID, 'carselect'))
# select_element.select_by_index(2)
# driver.save_screenshot("my_screen_1.png")
# select_element.select_by_visible_text("Benz")
# driver.save_screenshot("my_screen_2.png")
# driver.close()

# ----------
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.letskodeit.com/practice")

# driver.execute_script("window.open('')")

# before = driver.window_handles[0]
# after = driver.window_handles[1]

# driver.switch_to.window(after)
# driver.get("https://www.python.org/")
# print(driver.title)
# time.sleep(2)

# driver.switch_to.window(before)
# print(driver.title)
# time.sleep(2)

# driver.quit()

# ---------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time


# # Initialize the WebDriver
# driver = webdriver.Chrome()
# driver.set_page_load_timeout(2)

# # Open the desired webpage
# driver.get("https://www.python.org/")

# driver.maximize_window()
# time.sleep(3)

# # List of element IDs you want to wait for
# donate_element = (By.XPATH, '//a[text()="Donate"]')
# search_element = (By.ID, "id-search-field")
# member_element = (By.XPATH, '//a[text()="Become a Member"]')


# element_list = [donate_element, search_element, member_element]

# for element_locator in element_list:
#     try:
#         element = WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located(donate_element)
#         )
#         print(f"Element '{element}' is present")

#     except Exception as e:
#         print(f"Element '{element}' was not found: {e}")

# driver.close()


# ---------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.letskodeit.com/practice")
# driver.maximize_window()
# driver.set_page_load_timeout(20)

# driver.switch_to.frame("courses-iframe")
# search_element_locator = (By.XPATH, "//input[@id='search']")
# search_element = driver.find_element(*search_element_locator)

# action = ActionChains(driver)
# action.move_to_element(search_element)
# time.sleep(2)

# search_element.send_keys("Bla Bla")
# time.sleep(2)

# driver.switch_to.default_content()
# practice_page_title = (By.XPATH, '//h1[text()="Practice Page"]')
# practice_page_element = driver.find_element(*practice_page_title)
# print(practice_page_element.text)

# driver.close()


# ------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
driver.set_page_load_timeout(20)

alert_button_locator = (By.ID, 'alertbtn')
driver.find_element(*alert_button_locator).click()
popup = driver.switch_to.alert
print(popup.text)
time.sleep(2)
popup.accept()
time.sleep(2)
driver.close()
