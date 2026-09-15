import pytest
from lesson_38_homework import config
from pom.login import LetsKodeitLoginPage
from TestData import data


@pytest.mark.regression
def test_login(browser, test_logger):
    login_page = LetsKodeitLoginPage(browser)
    error_message = login_page.login(data.username, data.password, config.file_name)
    assert error_message, "No error message was returned."


@pytest.mark.smoke
def test_open_new_tab(browser, test_logger):
    login_page = LetsKodeitLoginPage(browser)
    login_page.open_new_tab()
    assert "google" in browser.current_url.lower()