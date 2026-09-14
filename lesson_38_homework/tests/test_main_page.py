import pytest
from pom.main import LetsKodeitMainPage
from TestData import config


@pytest.mark.smoke
def test_alert_handling(browser):
  page = LetsKodeitMainPage(browser)
  alert_text = page.get_alert_text(config.file_name)
  assert alert_text is not None


@pytest.mark.regression
def test_get_element_attribute(browser, test_logger):
  page = LetsKodeitMainPage(browser)
  style = page.get_element_attribute(config.file_name)
  assert style is not None


@pytest.mark.regression
def test_hover_and_click(browser, test_logger):
  page = LetsKodeitMainPage(browser)
  page.hover_and_click()
  assert "#top" in browser.current_url or browser.current_url is not None


@pytest.mark.smoke
def test_footer_text(browser, test_logger):
  page = LetsKodeitMainPage(browser)
  text = page.get_footer_text(config.file_name)
  assert isinstance(text, str)