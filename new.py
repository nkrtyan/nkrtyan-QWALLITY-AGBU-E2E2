from selenium_test import webdriver
from selenium.webdriver.common.by import By

browsers = ("Chrome",)


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

    # zeroWidthButton
    zero_width = driver.find_element(By.ID, "zeroWidthButton")

    if zero_width.is_displayed():
        print("zeroWidthButton is displayed")
    else:
        print("zeroWidthButton is not displayed")

    print(
        "zeroWidthButton style:",
        zero_width.get_attribute("style")
    )

    overlapped = driver.find_element(By.ID, "overlappedButton")

    print(
        "overlappedButton style:",
        overlapped.get_attribute("style")
    )

    # Other buttons
    buttons = (
        "removedButton",
        "transparentButton",
        "invisibleButton",
        "notdisplayedButton",
        "offscreenButton"
    )

    visibility_results = []

    for button_id in buttons:

        elements = driver.find_elements(By.ID, button_id)

        if not elements:
            result = (button_id, "removed")
        else:
            element = elements[0]

            result = (
                button_id,
                element.is_displayed(),
                element.get_attribute("style")
            )

        visibility_results.append(result)

    print(visibility_results)

    driver.quit()


if __name__ == "__main__":

    for browser in browsers:
        print(f"Running test on: {browser}")
        get_elements(browser)