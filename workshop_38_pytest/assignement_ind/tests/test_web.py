import pytest
from workshop_38_pytest.assignement_ind import config
from workshop_38_pytest.assignement_ind.pom.main_page  import Letskodeit_main_page
from workshop_38_pytest.assignement_ind.pom.sign_in_page import SignIn
from workshop_38_pytest.assignement_ind.pom.google_page import GooglePage


@pytest.mark.regression
def test_lets(browser, test_logger):

    #Create objects
    main_page_obj = Letskodeit_main_page(browser, test_logger)
    google_page_obj = GooglePage(browser, test_logger)
    sign_in_page_obj = SignIn(browser, test_logger)


    main_page_obj.go_to_page(config.url)
    main_page_obj.find_and_click(main_page_obj.alert_btn)
    alert_text = main_page_obj.accept_alert()
    main_page_obj.append_text_to_file(config.file_name, f'Alert text - {alert_text}')

    hide_atr = main_page_obj.hide_show_function()
    main_page_obj.append_text_to_file(config.file_name, f'Hidden attribute - {hide_atr}')
    
    main_page_obj.mouse_hover()
    f_text = main_page_obj.scroll_function()
    main_page_obj.append_text_to_file(config.file_name, f"Footer text - {f_text}")

    main_page_obj.click_sign_in_btn()
    validation_msg = sign_in_page_obj.sign_in()
    main_page_obj.append_text_to_file(config.file_name, f'Sign in validation message - {validation_msg}')

    google_page_obj.open_google_page()





# if __name__ == "__main__":
#     test_lets()

