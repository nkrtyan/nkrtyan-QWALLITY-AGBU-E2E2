from pages.practice_page import PracticePage
from pages.login_page import LoginPage

from helpers.test_helper import TestHelper
from helpers.logger import logger

from data import (
    WRONG_EMAIL,
    WRONG_PASSWORD,
    GOOGLE_URL
)


class TestPractice:

    def test_assignment_2(self, setup):

        driver = setup

        practice = PracticePage(driver)
        login = LoginPage(driver)

        logger.info("Test started")

        # 1. Alert
        practice.click_alert()

        alert_text = practice.get_alert_text()

        TestHelper.save_text(
            "Alert text:",
            alert_text,
            "w"
        )

        practice.accept_alert()

        TestHelper.screenshot(
            driver,
            "01_alert.png"
        )

        # 2. Hide textbox
        practice.hide_textbox()

        style = practice.get_textbox_attribute()

        TestHelper.save_text(
            "Hidden element style attribute:",
            style
        )

        TestHelper.screenshot(
            driver,
            "02_hidden_element.png"
        )

        # 3. Mouse Hover
        practice.move_to_mouse_hover()

        TestHelper.screenshot(
            driver,
            "03_mouse_hover.png"
        )

        # 4. Top
        practice.click_top()

        TestHelper.screenshot(
            driver,
            "04_top.png"
        )

        # 5. Footer
        footer = practice.get_footer_text()

        TestHelper.save_text(
            "Footer text:",
            footer
        )

        TestHelper.screenshot(
            driver,
            "05_footer.png"
        )

        # 6. Sign In
        practice.click_sign_in()

        TestHelper.screenshot(
            driver,
            "06_sign_in.png"
        )

        # 7. Incorrect login
        error = TestHelper.wrong_login(
            login,
            WRONG_EMAIL,
            WRONG_PASSWORD
        )

        TestHelper.save_text(
            "Login validation message:",
            error
        )

        TestHelper.screenshot(
            driver,
            "07_login_error.png"
        )

        # 8. Open Google in new tab
        TestHelper.open_google(
            driver,
            GOOGLE_URL
        )

        TestHelper.screenshot(
            driver,
            "08_google.png"
        )

        logger.info("Test finished successfully")