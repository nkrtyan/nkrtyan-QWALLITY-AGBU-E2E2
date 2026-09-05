from selenium import webdriver
from selenium.webdriver.common.by import By

browsers = ["Chrome"]


def get_elements(browser):

    if browser == "Chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()



    driver.get("http://www.uitestingplayground.com/")

    visibility = driver.find_element(By.XPATH, '//a[@href="/visibility"]')
    visibility.click()

                
    hide = driver.find_element(By.ID, "hideButton")
    hide.click()

    elements = [
            (
                "removedButton",
                "//button[@type='button' and @id='removedButton']"
            ),
            (
                "zeroWidth",
                "//button[@type='button' and @id='zeroWidthButton']"
            ),
            (
                "overlapped",
                "//div[contains(@style, 'position: absolute') "
                "and contains(@style, 'background-color: white')]"
            ),
            (
                "transparentButton",
                "//button[@type='button' and @id='transparentButton']"
            ),
            (
                "invisibleButton",
                "//button[@type='button' and @id='invisibleButton']"
            ),
            (
                "notdisplayedButton",
                "//button[@type='button' and @id='notdisplayedButton']"
            ),
            (
                "offscreenButton",
                "//button[@type='button' and @id='offscreenButton']"
            )
        ]

    for name, xpath in elements:
        try:
            element = driver.find_element(By.XPATH, xpath)

            if name == "removedButton":
                
                if not element.is_displayed():
                    raise Exception("Remove buttin is hidden")
        
            elif name == "overlapped_div":
                if element.is_displayed():
                    print("Overlapped button is not hidden")
                else:
                    raise Exception("Overlapped button is hidden")

            else:
                if not element.is_displayed():
                    print(f"{name}: hidden")
                else:
                    raise Exception(f"{name}: element is displayed")
           
    
        except Exception as error:
            print(f"{name} is not displayed or was removed")
            
if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")

        elements = get_elements(browser)
