from selenium import webdriver

from pages.practice_page import PracticePage
from pages.login_page import LoginPage
from helpers.screenshot_helper import ScreenshotHelper
from helpers.logger import logger


# Open browser
driver = webdriver.Chrome()
screenshot = ScreenshotHelper(driver)

try:
    # 1. Open website
    logger.info("Test started")

    driver.get("https://www.letskodeit.com/practice")
    driver.maximize_window()

    logger.info("Practice page opened")

    practice_page = PracticePage(driver)

    # 2. Alert Popup
    practice_page.click_alert_button()
    logger.info("Alert button clicked")

    popup_text = practice_page.get_alert_text()

    print("Popup text:", popup_text)
    logger.info(f"Popup text: {popup_text}")

    with open(
        "live_coding_text.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write("Popup text:\n")
        file.write(popup_text + "\n\n")

    practice_page.accept_alert()
    logger.info("Alert accepted")

    screenshot.take("01_alert")

    # 3. Hide Element
    hidden_element = practice_page.hide_element()

    attribute_name = "style"
    attribute_value = hidden_element.get_attribute(
        attribute_name
    )

    print("Attribute:", attribute_name)
    print("Value:", attribute_value)

    logger.info(
        f"Hidden element attribute: "
        f"{attribute_name}={attribute_value}"
    )

    with open(
        "live_coding_text.txt",
        "a",
        encoding="utf-8"
    ) as file:
        file.write("Hidden element:\n")
        file.write(f"Attribute: {attribute_name}\n")
        file.write(f"Value: {attribute_value}\n\n")

    screenshot.take("02_hidden_element")

    # 4. Mouse Hover -> Top
    practice_page.click_top_from_mouse_hover()

    print("Mouse Hover -> Top: PASSED")
    logger.info("Mouse Hover -> Top: PASSED")

    screenshot.take("03_mouse_hover_top")

    # 5. Footer
    footer_text = practice_page.get_footer_text()

    print("Footer text:")
    print(footer_text)

    logger.info(f"Footer text: {footer_text}")

    with open(
        "live_coding_text.txt",
        "a",
        encoding="utf-8"
    ) as file:
        file.write("Footer text:\n")
        file.write(footer_text + "\n\n")

    screenshot.take("04_footer")

    # 6. Sign In
    practice_page.click_sign_in()

    print("Sign In page opened")
    logger.info("Sign In page opened")

    screenshot.take("05_login")

    # 7. Sign In + Validation
    login_page = LoginPage(driver)

    validation_text = login_page.sign_in_and_validate(
        "wrongemail@test.com",
        "wrongpassword"
    )

    print("Validation message:", validation_text)
    logger.info(
        f"Validation message: {validation_text}"
    )

    with open(
        "live_coding_text.txt",
        "a",
        encoding="utf-8"
    ) as file:
        file.write("Validation message:\n")
        file.write(validation_text + "\n\n")

    screenshot.take("06_invalid_login")

    # 8. New Tab -> Google
    driver.switch_to.new_window("tab")

    print("New tab opened")
    logger.info("New tab opened")

    driver.get("https://www.google.com")

    print("Google opened in second tab")
    logger.info("Google opened in second tab")

    screenshot.take("07_google")

    # Finished
    print("\nAssignment 2 finished successfully.")
    logger.info("Assignment 2 finished successfully")

except Exception as error:

    print("ERROR:", error)
    logger.error(f"Test failed: {error}")

    screenshot.take("ERROR")

finally:

    logger.info("Browser closed")
    driver.quit()