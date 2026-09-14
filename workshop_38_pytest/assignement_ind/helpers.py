from selenium import webdriver
from workshop_37.assignement_ind import test_data
import logging

class Helper:

    def test_navigate_to_page(self, my_driver):
        my_driver.get(test_data.url)


    def test_close_browser(self, my_driver):
        if my_driver:
            my_driver.quit()


    def test_open_file(self, text, mode="w"):
        with open(test_data.file_name, mode) as file:
            file.write(text)

