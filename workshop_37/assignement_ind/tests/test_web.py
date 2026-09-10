from workshop_37.assignement_ind import test_data
from workshop_37.assignement_ind.helpers import Helper
from workshop_37.assignement_ind.pom.main_page import Letskodeit_main_page
from workshop_37.assignement_ind.pom.sign_in_page import Sign_in

if __name__ == "__main__":

    # Activate Chrome browser and open website
    helper = Helper()
    driver = helper.browser()
    helper.navigate_to_page(driver)


    # Create Main Page object
    main_page = Letskodeit_main_page(driver)

    # Run Main Page actions
    main_page.alert_click()
    main_page.hide_show_function()
    main_page.mouse_hover()
    main_page.scroll_function()


    # Create Sign In Page object
    sign_in_page = Sign_in(
        driver,
        test_data.username,
        test_data.my_password
    )

    # Run Sign In actions
    sign_in_page.sign_in()
    sign_in_page.open_other_tab()


    # Close browser
    helper.close_browser(driver)