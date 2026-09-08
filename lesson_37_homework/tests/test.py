# from Helpers.lib import Helper
# from pom.main import LetsKodeitMainPage
# from TestData import data

# if __name__ == "__main__":
    
#     helper_obj = Helper()
#     browser = helper_obj.browser()

#     main_page = LetsKodeitMainPage(browser)
#     helper_obj.navigate_to_page(browser)
#     main_page.get_element_attribute(data.file_name)



from Helpers.lib import Helper
from pom.main import LetsKodeitMainPage
from pom.login import LetsKodeitLoginPage
from TestData import data

if __name__ == "__main__":
    helper_obj = Helper()
    browser = helper_obj.browser()

    # Էջերի օբյեկտների ստեղծում
    main_page = LetsKodeitMainPage(browser)
    login_page = LetsKodeitLoginPage(browser)

    # 1. Բացում ենք կայքը
    helper_obj.navigate_to_page(browser)

    # 2. Գրում ենք element-ի attribute-ը ֆայլում
    main_page.get_element_attribute(data.file_name)

    # 3. Alert-ի տեքստը պահում ենք ֆայլում
    main_page.save_alert_text_to_file(data.file_name)

    # 4. Scroll, Hover և Top button click
    main_page.hover_and_click_top()

    # 5. Footer-ի տեքստը գրում ենք ֆայլում
    main_page.write_footer_text(data.file_name)

    # 6. Փորձում ենք մուտք գործել սխալ տվյալներով
    login_page.login_with_invalid_data("test@gmail.com", "dadadadada", data.file_name)

    # 7. Բացում ենք Google-ը նոր tab-ում
    login_page.open_google_in_new_tab()

    # Փակում ենք բրաուզերը
    browser.quit()