from selenium import webdriver
import pytest
import logging
import os
from datetime import datetime


@pytest.fixture()
def get_driver():
    try:
        # Run Chrome in headless mode
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless=new')
        # options.add_argument('--window-size=1920,1080')
        # driver = webdriver.Chrome(options=options)

        # Open a visible browser window and maximize it
        browser = webdriver.Chrome()
        browser.maximize_window()
        yield browser
    except Exception as e:
        logging.error(f'Failed to set up driver: {e}')
        raise
    finally:
        if browser:
            browser.quit()


@pytest.fixture()
def test_logger(request):
    current_date = datetime.today().date()
    current_test = request.node.name
    log_folder = f"logs_{current_date}"

    try:
        os.makedirs(log_folder, exist_ok=True)
        log_file = f"{log_folder}/{current_test}.log"

        logging.basicConfig(
            filename=log_file,
            filemode="w+",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True
        )
    except Exception as e:
        logging.error(f'Failed to set up logger: {e}')
        raise

    # used by helpers.py to save a screenshot under logs_<date>/screenshots/<test_name>.png on failure
    logging.test_name = current_test
    logging.screenshot_dir = f"{log_folder}/screenshots"

    logging.info(f"{current_test} is started")
    yield logging
    logging.info(f"{current_test} is finished")