import logging
import pytest
from selenium import webdriver
from TestData import config
import os
from datetime import datetime


@pytest.fixture
def test_logger(request):
    try:
        today_date = datetime.today().date()
        os.makedirs(f"logs_{today_date}", exist_ok=True)

        test_name = request.node.name
        log_path = f"logs_{today_date}/{test_name}.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            filename=log_path,
            filemode='a+',
            encoding='utf-8',
            force=True
        )

        logging.info(f"{test_name} has started")
        yield
        logging.info(f"{test_name} has finished")

    except Exception as e:
        print("Driver opening failed: {e}")


@pytest.fixture
def browser():
    try:
        logging.info("Browser is opening...")
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
        logging.info("Browser is closed")
    except:
        print("Browser has failed")
