from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# 1. Open browser
driver = webdriver.Chrome()

# 2. Open website
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
time.sleep(2)


# 3. Click Alert button
alert_button = driver.find_element(By.ID, "alertbtn")
alert_button.click()


# 4. Get Alert text
alert = driver.switch_to.alert
popup_text = alert.text

print("Popup text:", popup_text)

alert.accept()
time.sleep(1)


# 5. Open text file
with open("live_coding_text.txt", "w", encoding="utf-8") as file:

    file.write("Popup text:\n")
    file.write(popup_text + "\n\n")


    # 6. Hide Textbox and get attribute
    displayed_element = driver.find_element(By.ID, "displayed-text")

    hide_button = driver.find_element(By.ID, "hide-textbox")
    hide_button.click()

    time.sleep(1)

    attribute_name = "style"
    attribute_value = displayed_element.get_attribute(attribute_name)

    print("Attribute:", attribute_name)
    print("Value:", attribute_value)

    file.write("Hidden element:\n")
    file.write(f"Attribute: {attribute_name}\n")
    file.write(f"Value: {attribute_value}\n\n")


    # 7. Mouse Hover
    mouse_hover_button = driver.find_element(By.ID, "mousehover")

    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover_button).perform()

    time.sleep(1)

    top_option = driver.find_element(
        By.XPATH,
        '//a[normalize-space()="Top"]'
    )

    top_option.click()

    time.sleep(1)


    # 8. Scroll to Footer and get Footer text
    footer = driver.find_element(By.TAG_NAME, "footer")

    driver.execute_script(
        "arguments[0].scrollIntoView();",
        footer
    )

    time.sleep(1)

    footer_text = footer.text

    print("Footer text:")
    print(footer_text)

    file.write("Footer text:\n")
    file.write(footer_text + "\n\n")


# 9. Go to Sign In
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(1)

sign_in_button = driver.find_element(
    By.XPATH,
    '//a[@href="/login"]'
)

sign_in_button.click()

time.sleep(3)


# 10. Login

email_field = driver.find_element(
    By.XPATH,
    '//input[@type="email"]'
)

password_field = driver.find_element(
    By.XPATH,
    '//input[@type="password"]'
)

email_field.send_keys("wrong@email.com")
password_field.send_keys("wrongpassword")

login_button = driver.find_element(
    By.XPATH,
    '//*[@id="login"]'
)

login_button.click()

time.sleep(2)


# 11. Get validation message
validation_message = driver.find_element(
    By.XPATH,
    '//div[contains(@class, "alert")]'
).text

print("Validation message:", validation_message)

with open("live_coding_text.txt", "a", encoding="utf-8") as file:
    file.write("Validation message:\n")
    file.write(validation_message + "\n\n")


# 12. Open new tab
driver.switch_to.new_window("tab")


# 13. Open Google
driver.get("https://www.google.com")

time.sleep(10)


# Close browser
driver.quit()