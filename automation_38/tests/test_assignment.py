import config
import testdata
import pytest
from pages.practice_page import PracticePage
from pages.sign_in_page import SignInPage


@pytest.mark.smoke
@pytest.mark.regression
def test_assignment_2(get_driver, test_logger):
    # Create page objects
    practice_page = PracticePage(get_driver, test_logger)
    sign_in_page = SignInPage(get_driver, test_logger)

    # 1. Navigate to Practice Page
    practice_page.go_to_page(config.practice_url)

    # 2. Open alert and get text
    alert_text = practice_page.open_alert_and_get_text()
    assert alert_text, "Alert text should not be empty"
    practice_page.append_text_to_file(config.output_file, alert_text + "\n")

    # 3. Hide element and check visibility
    hide_attr = practice_page.hide_element_and_get_visibility_attribute()
    assert "display: none" in hide_attr, "Textbox should be hidden"

    practice_page.append_text_to_file(config.output_file, "HIDE/SHOW ELEMENT ATTRIBUTE")
    practice_page.append_text_to_file(config.output_file, f"style = {hide_attr}\n")

    # 4. Mouse hover -> Top
    practice_page.hover_and_click_top()

    # 5. Move to footer
    footer_text = practice_page.get_footer_text()
    assert footer_text, "Footer text should not be empty"

    practice_page.append_text_to_file(config.output_file, "FOOTER TEXT")
    practice_page.append_text_to_file(config.output_file, footer_text + "\n")

    # 6. Click Sign In
    practice_page.click_sign_in()

    # 7. Fill incorrect email/password
    sign_in_page.login_with_invalid_credentials(
        testdata.invalid_email,
        testdata.invalid_password
    )

    # 8. Get validation message
    validation_message = sign_in_page.get_validation_message()
    assert validation_message, "Validation message should not be empty"

    practice_page.append_text_to_file(config.output_file, "LOGIN VALIDATION MESSAGE")
    practice_page.append_text_to_file(config.output_file, validation_message + "\n")

    # 9. Open a new tab, switch to it and get google.com
    google_url = sign_in_page.open_google_in_new_tab(config.google_url)
    assert "google" in google_url.lower(), "Second tab should contain Google"

    practice_page.append_text_to_file(config.output_file, "SECOND TAB URL")
    practice_page.append_text_to_file(config.output_file, google_url)
