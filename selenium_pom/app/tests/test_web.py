"""
1. Open Chrome browser
2. Navigate to https://www.letskodeit.com/practice
3. Click to open the Alert popup
4. Get text from the popup
5. Open txt file with live_coding_text.txt file name and write there popup text
6. Locate the mentioned element, hide it, and then add the attribute and its value,
   based on which it shows and hides, to the text file
7. Move to Mouse Hover button, click on it and Click on Top option to go to the top of screen
8. Move to the footer and write text in the opened file
9. Click on the Sign In button
10. Fill the fields with incorrect email or password and click the LogIn button
11. Get validation message and write in the txt file
12. Open a new tab, switch to the new tab
13. Get google.com on the second tab
"""

import os
import sys

# Make the project root importable regardless of how/where this file is run from
# (VS Code "Run", `python3 app/tests/test_web.py`, pytest, etc.)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.Helpers.helper import Helper
from app.pom.practice_page import PracticePage
from app.pom.login_page import LoginPage
from app.TestData import data
from app.Helpers.logger import get_logger

logger = get_logger(__name__)

def test_live_coding():
    logger.info("===Starting test_live_coding===")
    helper = Helper()
    browser = helper.get_browser()

    try:
        # 1-2. Open Chrome and navigate to the practice page
        helper.navigate_to(browser, data.url)
        logger.info(f"Navigated to {data.url}")
        practice_page = PracticePage(browser)

        # 3-5. Open the alert, read its text, accept it, and log the text
        practice_page.open_alert()
        popup_text = practice_page.get_and_accept_alert_text()
        logger.info(f"Alert text captured:{popup_text}")
        helper.write_to_file(data.output_file, popup_text, mode="w")

        # 6. Hide the element and log the attribute that controls show/hide
        practice_page.hide_displayed_text()
        style_attribute = practice_page.get_hidden_element_style()
        logger.info(f"Hidden element style: {style_attribute}")
        helper.write_to_file(data.output_file, style_attribute)

        # 7. Hover over "Mouse Hover" then click "Top"
        practice_page.hover_mouse_and_click_top()
        logger.info("Hovered and clicked Top")

        # 8. Scroll to the footer and log its text
        footer_text = practice_page.scroll_to_footer_and_get_text()
        logger.info(f"Footer text: {footer_text}") 
        helper.write_to_file(data.output_file, footer_text)

        # 9. Click Sign In
        practice_page.click_sign_in()
        logger.info("Clicked Sign In") 

        # 10-11. Submit invalid credentials and log the validation message
        login_page = LoginPage(browser)
        login_page.login(data.wrong_email, data.wrong_password)
        validation_message = login_page.get_validation_message()
        logger.info(f"Validation message: {validation_message}")
        helper.write_to_file(data.output_file, validation_message)

        # 12-13. Open a second tab, switch to it, and navigate to google.com
        helper.open_new_tab_and_navigate(browser, data.second_tab_url)
        logger.info("Opened second tab and navigated to google.com")
        logger.info("=== test_live_coding completed successfully ===")

    finally:
        helper.close_browser(browser)
        logger.info("Browser closed")   


if __name__ == "__main__":
    test_live_coding()
