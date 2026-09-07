from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""1. Open Chrome browser
2. Navigate to https://www.letskodeit.com/practice
3. Click to open the Alert popup
4. Get text from the popup
5. Open txt file with live_coding_text.txt file name and write there popup text
6. Locate the mentioned element, hide it, and then add the attribute and its value, based on which it shows and hides, to
the text file
7. Move to Mouse Hover button, click on it and Click on Top option to go to the top of screen
8. Move to the footer and write text in the opened file
9. Click on the Sign In button
10. Fill the fields with incorrect email or password and click the LogIn button
11. Get validation message and write in the txt file
12. Open a new tab, switch to the new tab
13. Get google.com on the second tab

"""


my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("https://www.letskodeit.com/practice")

# 3. Click to open the Alert popup
# 4. Get text from the popup
# 5. Open txt file with live_coding_text.txt file name and write there popup text
click_alert = my_driver.find_element(By.XPATH, '//input[@id = "alertbtn"]')
click_alert.click()
popup_text = my_driver.switch_to.alert
print(popup_text.text)

with open("live_coding_text.txt", "w") as file:
    file.write(popup_text.text)

popup_text.accept()

# 6. Locate the mentioned element, hide it, and then add the attribute and its value, based on which it shows and hides, to the text file
hide_show_element = my_driver.find_element(By.XPATH, '//input[@id = "displayed-text"]')
hide_btn = my_driver.find_element(By.XPATH, '//input[@id = "hide-textbox"]')
hide_btn.click()
changed_attribute = my_driver.find_element(By.XPATH, '//input[starts-with(@style, "display:")]')

print(changed_attribute.get_attribute('style'))
with open("live_coding_text.txt", "a") as file:
    file.write("\n")
    ##TODO can't add attribute to the text
    file.write(changed_attribute.get_attribute('style'))


# 7. Move to Mouse Hover button, click on it and Click on Top option to go to the top of screen
mouse_hove_btn = my_driver.find_element(By.XPATH, '//button[@id = "mousehover"]')
mouse_hove_btn.click()
time.sleep(2)
mouse_btn_top = my_driver.find_element(By.XPATH, '//a[text()= "Top"]')
actions = ActionChains(my_driver)
actions.move_to_element(mouse_btn_top).perform()

# 8. Move to the footer and write text in the opened file
scroll_footer = my_driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/span/div/div[1]/div/div[1]/p")
my_driver.execute_script(
    "arguments[0].scrollIntoView();",
    scroll_footer)
time.sleep(2)
with open("live_coding_text.txt", "a") as file:
    file.write("\n")
    file.write(scroll_footer.text)

# 9. Click on the Sign In button
# 10. Fill the fields with incorrect email or password and click the LogIn button
# 11. Get validation message and write in the txt file
sign_in_btn = my_driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/span[2]/div/div/a')
sign_in_btn.click()
e_mail = my_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/input')
e_mail.click()
e_mail.send_keys("bla-Blaghhk")
password = my_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div[3]/div/div/input')
password.click()
password.send_keys('11111111')
my_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div[5]/div[1]/button').click()
validation_message = WebDriverWait(my_driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/span')))
with open("live_coding_text.txt", "a") as file:
    file.write("\n")
    file.write(validation_message.text)


# 12. Open a new tab, switch to the new tab
# 13. Get google.com on the second tab
my_driver.execute_script("window.open('')")
before = my_driver.window_handles[0]
after = my_driver.window_handles[1]
my_driver.switch_to.window(after)
time.sleep(2)
my_driver.get("google.com")
time.sleep(2)
