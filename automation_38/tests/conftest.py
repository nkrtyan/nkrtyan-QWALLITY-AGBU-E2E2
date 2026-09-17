import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
import os
from datetime import datetime
import pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = None
    try:
        # AZURE / HEADLESS MODE
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        # options.add_argument("--window-size=1920,1080")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # driver = webdriver.Chrome(options=options)

        # --- LOCAL MODE/ browser

        driver = webdriver.Chrome()
        driver.maximize_window()

        yield driver
    except Exception as e:
        logging.error(f"Failed to set up driver: {e}")
        raise
    finally:
        if driver:
            driver.quit()


@pytest.fixture()
def test_logger(request):
    today_date = datetime.today().date()
    test_name = request.node.name
    logs_dir = f"logs_{today_date}"

    try:
        os.makedirs(f"{logs_dir}/screenshots", exist_ok=True)
        log_path = f"{logs_dir}/{test_name}.log"

        logging.basicConfig(
            filename=log_path,
            filemode="w+",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True,
        )
    except Exception as e:
        logging.error(f"Failed to set up logger: {e}")
        raise

    logging.test_name = test_name
    logging.screenshot_dir = f"{logs_dir}/screenshots"

    logging.info(f"{test_name} is started")
    yield logging
    logging.info(f"{test_name} is finished")
