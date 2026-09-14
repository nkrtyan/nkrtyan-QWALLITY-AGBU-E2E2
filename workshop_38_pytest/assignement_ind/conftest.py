from selenium import webdriver
import pytest
import logging
import os
from datetime import datetime

@pytest.fixture()
def browser (self):
    try:
        my_driver = webdriver.Chrome()
        my_driver.maximize_window()
        yield my_driver
        my_driver.quit()
        logging.info("Chrome browser activated")
        
    except:
        print("Error")

@pytest.fixture()
def test_loger(request):
    today_date = datetime.today().date()
    os.makedirs(f"logs_{today_date}", exist_ok=True)

    test_name = request.node.name
    log_path = f"logs{today_date}/{test_name}.log"

    logging.basicConfig(
    filename=log_path,
    filemode='w+', 
    level=logging.INFO,  
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%m-%d-%Y', 
    force=True
)

    logging.info(f"{test_name} is started")
    yield logging
    logging.info(f"{test_name} is finished")