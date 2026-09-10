from selenium import webdriver
from workshop_37.assignement_ind import test_data
import logging

class Helper:

    def browser (self):
        my_driver = webdriver.Chrome()
        my_driver.maximize_window()
        return my_driver
    

    def navigate_to_page(self, my_driver):
        my_driver.get(test_data.url)


    def close_browser(self, my_driver):
        if my_driver:
            my_driver.quit()


    def open_file(self, text, mode="w"):
        with open(test_data.file_name, mode) as file:
            file.write(text)

    def setup_logging():
        logging.basicConfig(
        level=logging.INFO,  
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m-%d-%Y', 
        filename='logging_file.log', 
        filemode='w',  
	    encoding='utf-8'  
)