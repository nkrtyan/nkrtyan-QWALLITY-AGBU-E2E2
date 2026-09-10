"""
FULL WORKED EXAMPLE — a small, realistic Selenium script
============================================================
This ties together: webdriver setup, locators, explicit waits, form
interaction, assertions, logging, and teardown. Use this as a template
you can adapt quickly under exam time pressure.

To actually run this you need:
    pip install selenium
and a matching browser driver on PATH (or use Selenium Manager, which
modern Selenium versions ship with automatically).
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- logging setup: so you get a record of what happened, not just print() ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def run_login_test():
    """
    Example flow:
    1. Open the browser and navigate to a page
    2. Wait for + locate the username/password fields
    3. Fill the form and submit
    4. Wait for + assert the expected result
    5. Always clean up the browser session, even if something fails
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)   # reusable explicit-wait object, 10s timeout

    try:
        log.info("Navigating to the login page")
        driver.get("https://the-internet.herokuapp.com/login")

        log.info("Waiting for the username field to be present")
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")

        log.info("Filling in credentials")
        username_field.clear()
        username_field.send_keys("tomsmith")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")

        log.info("Submitting the form")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        log.info("Waiting for the success message to appear")
        success_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )

        # A basic assertion — the kind of check an exam question often wants
        assert "You logged into a secure area" in success_message.text, \
            "Expected success message not found!"
        log.info("Login test PASSED")

    except Exception as e:
        log.error(f"Login test FAILED: {e}")
        driver.save_screenshot("login_test_failure.png")   # capture evidence on failure
        raise   # re-raise so the test runner still reports it as a failure

    finally:
        log.info("Closing the browser")
        driver.quit()   # ALWAYS clean up, whether the test passed or failed


# --- a pytest-style version, in case the exam wants a test function ---
"""
import pytest

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d               # give the driver to the test
    d.quit()              # runs after the test finishes (pass or fail) — like a context manager

def test_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    assert "You logged into a secure area" in success.text
"""


if __name__ == "__main__":
    run_login_test()
