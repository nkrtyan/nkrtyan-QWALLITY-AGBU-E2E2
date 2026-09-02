from selenium import webdriver
from selenium.webdriver.common.by import By

browsers = ["chrome"]

def get_elements(browser):
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    try:
        driver.get("https://www.letskodeit.com/practice")


        radio = driver.find_elements(By.CSS_SELECTOR, "input#benzradio")
        checkbox = driver.find_elements(By.XPATH, '//input[@id="hondacheck"]')
        open_tab = driver.find_elements(By.XPATH, '//a[@target="_blank" and @id="opentab"]')
        selectors  = driver.find_elements(By.XPATH, '//select/option[@value="orange" or @value="peach"]')
        btn = driver.find_elements(By.CSS_SELECTOR, 'input#show-textbox')
        hide = driver.find_elements(By.CSS_SELECTOR, 'input[name="show-hide"]')
        alert = driver.find_elements(By.CSS_SELECTOR, 'input[placeholder="Enter Your Name"]')
        hover = driver.find_elements(By.XPATH, "//legend[text()='Mouse Hover Example']")
        table = driver.find_elements(By.XPATH, '//td[text()="Python Programming Language"]')

        actions = [radio, checkbox,open_tab,selectors ,btn,hide,alert,hover,table]

        return actions
        

    except Exception as error:
        print(f"[{browser}] Test ERROR: {error}")

    finally:
        driver.quit()
    
    
def counter(actions):
    count = 0
    for item in actions:
        count += len(item)

    print(count)

    

if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")
        actions = get_elements(browser)
        counter(actions)