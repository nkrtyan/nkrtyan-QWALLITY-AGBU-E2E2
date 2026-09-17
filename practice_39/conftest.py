from selenium import webdriver
import pytest
import logging
import os
from datetime import datetime


@pytest.fixture()
def get_driver():
    driver = None

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)
        yield driver

    except Exception as e:
        logging.error(f"Driver error: {e}")
        raise

    finally:
        if driver:
            driver.quit()


@pytest.fixture()
def test_logger(request):
    test_name = request.node.name
    logs_dir = f"logs_{datetime.today().date()}"

    try:
        os.makedirs(logs_dir, exist_ok=True)

        logging.basicConfig(
            filename=f"{logs_dir}/{test_name}.log",
            filemode="w",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True
        )

        logging.test_name = test_name
        logging.screenshot_dir = f"{logs_dir}/screenshots"

        logging.info(f"{test_name} started")

        yield logging

        logging.info(f"{test_name} finished")

    except Exception as e:
        logging.error(f"Logger error: {e}")
        raise