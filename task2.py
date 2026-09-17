from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def qa_testing(button):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")

    alertbtn = driver.find_element(By.XPATH, "//input[@id='alertbtn']")
    alertbtn.click()

    alert = driver.switch_to.alert
    print(alert.text)
    alert_text = alert.text
    

    with open("live_coding_text.txt", "w") as file:
        file.write(alert_text)
    alert.accept()

    


    show_button = driver.find_element(By.XPATH, "//input[@name='show-hide']")
    hide_button = driver.find_element(By.XPATH, "//input[@value='Hide']")
    hide_button.click()

    style_value =show_button.get_attribute("style")

    print(style_value)

    with open("live_coding_text.txt", "a") as file:
        file.write(f"\nstyle = {style_value}")

    mouse_hover = driver.find_element(By.XPATH, "//button[contains(text(), 'Mouse Hover')]")
    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover).perform()
    print("Mouse Hover clicked")
   

    top_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Top')]")
    top_button.click()
    print("Top button clicked")

    
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    footer = driver.find_element(By.XPATH, "//p[contains(@class, 'jqCopyRight')]")
    footer_text = footer.text
    print(footer_text)

    with open("live_coding_text.txt", "a") as file:
        file.write(f"\n{footer_text}")

    

    sign_in = driver.find_element(By.XPATH, "//a[@href='/login']")
    sign_in.click()

    email = driver.find_element(By.XPATH, "//input[@name='email' and @type='email']")
    email.send_keys("gay@mail.com")
    
    password = driver.find_element(By.XPATH, "//input[@name='password' and @type='password']")
    password.send_keys("11223344")
    
    login_btn = driver.find_element(By.XPATH, "//button[@id='login' and @type='button']")
    login_btn.click()
    
    login_btn.click()

    validation_message = driver.find_element(By.XPATH, "//span[@id='incorrectdetails']").text
    print(validation_message)
    with open("live_coding_text.txt", "a") as file:
        file.write(f"\n{validation_message}")

    driver.switch_to.new_window("tab")
    driver.get("https://www.google.com")

    driver.quit()

qa_testing("alert")