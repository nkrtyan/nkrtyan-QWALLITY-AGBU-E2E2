import config
import pytest
from Pages.practice_page import PracticePage
from Pages.google_page import GooglePage
from Pages.sign_in_page import SignIn


@pytest.mark.regression
def test_lets(get_driver, test_logger):

    # Create objects
    practice_page_obj = PracticePage(get_driver, test_logger)
    google_page_obj = GooglePage(get_driver, test_logger)
    sign_in_page_obj = SignIn(get_driver, test_logger)

    practice_page_obj.go_to_page(config.practice_url)

    practice_page_obj.find_and_click(practice_page_obj.alert_button)
    alert_text = practice_page_obj.accept_alert()
    practice_page_obj.append_text_to_file(
        config.output_file,
        f'Alert text - {alert_text}'
    )

    hidden_style = practice_page_obj.check_hide_element()
    practice_page_obj.append_text_to_file(
        config.output_file,
        f'Hidden attribute - {hidden_style}'
    )

    practice_page_obj.check_mouse_hover()

    footer_value = practice_page_obj.get_footer_text()
    practice_page_obj.append_text_to_file(
        config.output_file,
        f'Footer text - {footer_value}'
    )

    practice_page_obj.click_sign_in()
    validation_msg = sign_in_page_obj.sign_in()
    practice_page_obj.append_text_to_file(
        config.output_file,
        f'Sign in validation message - {validation_msg}'
    )

    google_page_obj.go_to_google()