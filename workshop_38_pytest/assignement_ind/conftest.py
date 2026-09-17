from selenium import webdriver
import pytest
import logging
import os
from datetime import datetime

@pytest.fixture()
def browser ():
    try:
        my_driver = webdriver.Chrome()
        my_driver.maximize_window()
        
        logging.info("Chrome browser activated")

        yield my_driver

        
    except Exception as e:
         logging.error(f'Failed to set up driver: {e}')
         raise

    finally:
        if my_driver:
            my_driver.quit()



@pytest.fixture()
def test_logger(request):
    today_date = datetime.today().date()
    test_name = request.node.name
    logs_dir = f"logs_{today_date}"
    

    try:
        os.makedirs(f"logs_{today_date}", exist_ok=True)
        log_path = f"logs_{today_date}/{test_name}.log"

        logging.basicConfig(
        filename=log_path,
        filemode='w+', 
        level=logging.INFO,  
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m-%d-%Y', 
        force=True
    )
    except Exception as e:
        logging.error(f'Failed to set up logger: {e}')
        raise

    logging.test_name = test_name
    logging.screenshot_dir = f"{logs_dir}/screenshots"

    logging.info(f"{test_name} is started")
    yield logging
    logging.info(f"{test_name} is finished")

    logging.info(f"{test_name} is started")
    yield logging
    logging.info(f"{test_name} is finished")