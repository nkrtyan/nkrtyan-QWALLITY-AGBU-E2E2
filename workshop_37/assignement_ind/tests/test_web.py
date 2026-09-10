import logging
from workshop_37.assignement_ind import test_data
from workshop_37.assignement_ind.helpers import Helper
from workshop_37.assignement_ind.pom.main_page import Letskodeit_main_page
from workshop_37.assignement_ind.pom.sign_in_page import Sign_in

if __name__ == "__main__":

    helper = Helper()
    driver = None

    try:

        # Activate logging
        helper.setup_logging()

        # Activate Chrome browser and open website
        driver = helper.browser()
        logging.info("Chrome browser activated")

        helper.navigate_to_page(driver)
        logging.info("Website opened")

        # Create Main Page object
        main_page = Letskodeit_main_page(driver)

        # Run Main Page actions
        main_page.alert_click()
        logging.info("Alert action completed")

        main_page.hide_show_function()
        logging.info("Hide/Show action completed")

        main_page.mouse_hover()
        logging.info("Mouse hover action completed")

        main_page.scroll_function()
        logging.info("Scroll action completed")

        # Create Sign In Page object
        sign_in_page = Sign_in(
            driver,
            test_data.username,
            test_data.my_password
        )

        # Run Sign In actions with incorrect credentials
        sign_in_page.sign_in()
        logging.info("Sign In completed unsuccessfully, Validation mesage shown")

        # Opening other tab and website
        sign_in_page.open_other_tab()
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

