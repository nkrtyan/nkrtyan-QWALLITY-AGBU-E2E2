from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browsers = ["Chrome"]

def task2():
    try:

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://www.letskodeit.com/practice")

        #Get text from alert and save in txt file

        open_alert = driver.find_element(By.ID, 'alertbtn').click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

        with open("live_coding_text.txt", "w", encoding="utf-8") as file:
            file.write(alert_text+ "\n")


        #Get element attribute 
        element = driver.find_element(By.ID, "displayed-text")

        driver.execute_script("arguments[0].style.display = 'none';",element)

        style_value = element.get_attribute("style")

        with open("live_coding_text.txt", "a", encoding="utf-8") as file:
            file.write("style = " + style_value + "\n")

        #Move to hover btn and click to top
        hover_btn = driver.find_element(By.XPATH, '//button[@id="mousehover"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", hover_btn)
        actions = ActionChains(driver)
        actions.move_to_element(hover_btn).perform()

        top_btn = driver.find_element(By.XPATH, '//a[@href="#top"]').click()


        #Move to the footer and write text in the opened file
        footer = driver.find_element(By.XPATH,"//p[contains(@class, 'jqCopyRight')]")

        driver.execute_script("arguments[0].scrollIntoView();",footer)

        footer_text = footer.text

        with open("live_coding_text.txt", "a", encoding="utf-8") as file:
            file.write("\n" + footer_text)

        #Sign in with invalid data and get error text
        signin_btn = driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        email = driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@gmail.com")
        password = driver.find_element(By.XPATH, "//input[@name='password']").send_keys("dadadadada")
        login_btn = driver.find_element(By.XPATH, "//button[@id='login']").click()
        error_msg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='incorrectdetails']")))
        validation_message = error_msg.text

        with open("live_coding_text.txt", "a", encoding="utf-8") as file:
            file.write("\n" + validation_message)

        #OPen new tab, redirect to new tab and open google.com
        driver.execute_script("window.open('')")
        before = driver.window_handles[0]
        after = driver.window_handles[1]
        driver.switch_to.window(after)
        driver.get("https://www.google.com/")

    except Exception as error:
        print(f"[{browser}] Test ERROR: {error}")

    finally:
        driver.quit()
if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")
        task2()