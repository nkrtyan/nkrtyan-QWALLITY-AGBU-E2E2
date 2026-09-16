import logging
import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture
def browser():
    try:
        # Run Chrome in headless mode
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless=new')
        # options.add_argument('--window-size=1920,1080')
        # driver = webdriver.Chrome(options=options)

        # Open a visible browser window and maximize it
        logging.info("Browser is opening ...")
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        logging.info("Browser is closed")
    except Exception as e:
        print(f'Failed to set up driver: {e}')
    finally:
        if driver:
            driver.quit()

@pytest.fixture
def test_logger(request):

    today_date = datetime.today().date()
    test_name = request.node.name
    logs_dir = f"logs_{today_date}"

    try:
        os.makedirs(f"logs_{today_date}", exist_ok=True)
        log_path = f"logs_{today_date}/{test_name}.log"

        logging.basicConfig(
            level=logging.INFO,   
            format='%(asctime)s [%(levelname)s] %(message)s',   
            filename= log_path,
            filemode='a+',
            encoding='utf-8',
            force=True
        )

    except Exception as e:
        logging.error(f'Failed to set up logger: {e}')
        raise


# used by lib.py to save a screenshot under logs_<date>/screenshots/<test_name>.png on failure
    logging.test_name = test_name
    logging.screenshot_dir = f"{logs_dir}/screenshots"

    logging.info(f"{test_name} is started")
    yield logging
    logging.info(f"{test_name} is finished")

