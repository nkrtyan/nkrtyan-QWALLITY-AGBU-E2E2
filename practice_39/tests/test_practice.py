import config
import pytest

from pages.practice_page import PracticePage
from pages.google_page import GooglePage
from pages.sign_in_page import SignIn


@pytest.mark.regression
def test_lets(get_driver, test_logger):

    practice_page = PracticePage(get_driver, test_logger)
    google_page = GooglePage(get_driver, test_logger)
    sign_in_page = SignIn(get_driver, test_logger)
    practice_page.go_to_page(config.practice_url)
    practice_page.find_and_click(practice_page.alert_btn)
    alert_text = practice_page.accept_alert()
    practice_page.append_text_to_file(config.output_file, f"Alert text - {alert_text}")
    hide_attr = practice_page.hide_element_check()
    practice_page.append_text_to_file(config.output_file, f"Hidden attribute - {hide_attr}")
    practice_page.mouse_hover_check()
    footer_text = practice_page.footer_text()
    practice_page.append_text_to_file(config.output_file,f"Footer text - {footer_text}")
    practice_page.click_sign_in_btn()
    validation_msg = sign_in_page.sign_in()
    practice_page.append_text_to_file(config.output_file, f"Sign in validation message - {validation_msg}")

    google_page.open_google_page()