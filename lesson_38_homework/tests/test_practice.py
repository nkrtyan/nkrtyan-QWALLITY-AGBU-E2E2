import pytest
import config
from pom.main import LetsKodeitMainPage
from pom.login import LetsKodeitLoginPage
from pom.google import GooglePage

@pytest.mark.regression
def test_letskodit(browser, test_logger):

    # Create objects
    main_page_obj = LetsKodeitMainPage(browser, test_logger)
    google_page_obj = GooglePage(browser, test_logger)
    login_page_obj = LetsKodeitLoginPage(browser, test_logger)

    main_page_obj.navigate_to_page(config.url)
    main_page_obj.wait_and_click(main_page_obj.open_alert)
    alert_text = main_page_obj.get_and_accept_alert_text()
    main_page_obj.write_to_file(config.file_name, f'Alert text - {alert_text}')

    hide_attr = main_page_obj.wait_and_get_attribute(main_page_obj.element_locator, "style")
    main_page_obj.write_to_file(config.file_name, f'Hidden attribute - {hide_attr}')

    main_page_obj.hover_and_click()

    footer_text = main_page_obj.get_footer_text()
    main_page_obj.write_to_file(config.file_name, f'Footer text - {footer_text}')

    main_page_obj.click_sign_in_btn()
    error_msg = login_page_obj.login()
    main_page_obj.write_to_file(config.file_name, f'Sign in validation message - {error_msg}')

    google_page_obj.open_google_page()
