import logging
from workshop_38_pytest.assignement_ind import test_data
from workshop_38_pytest.assignement_ind.helpers import Helper
from workshop_38_pytest.assignement_ind.pom.main_page import Test_letskodeit_main_page
from workshop_38_pytest.assignement_ind.pom.sign_in_page import Test_sign_in

if __name__ == "__main__":

    helper = Helper()
    driver = None

    try:

        # # Activate logging
        # helper.setup_logging()

        # Activate Chrome browser and open website
        helper.test_navigate_to_page(driver)
        logging.info("Website opened")

        # Create Main Page object
        main_page = Test_letskodeit_main_page(driver)

        # Run Main Page actions
        main_page.test_alert_click()
        
        main_page.test_hide_show_function()
        

        main_page.test_mouse_hover()
        logging.info("Mouse hover action completed")

        main_page.test_scroll_function()
        logging.info("Scroll action completed")

        # Create Sign In Page object
        sign_in_page = Test_sign_in(
            driver,
            test_data.username,
            test_data.my_password
        )

        # Run Sign In actions with incorrect credentials
        sign_in_page.test_sign_in()
        logging.info("Sign In completed unsuccessfully, Validation mesage shown")

        # Opening other tab and website
        sign_in_page.test_open_other_tab()
        logging.info("New tab opened successfully")

        logging.info("Test execution completed successfully")

    except Exception as e:
        logging.error("Test execution failed: %s", e)
        if driver:
            driver.save_screenshot("error.png")

        raise


    finally:
        # Close browser
        if driver:
            helper.close_browser(driver)
            logging.info("Browser closed")

