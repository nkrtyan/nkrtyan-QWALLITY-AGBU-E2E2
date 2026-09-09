# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).resolve().parent.parent))
#python -m tests.test  
from Helpers.lib import Helper
from pom.main import LetsKodeitMainPage
from pom.login import LetsKodeitLoginPage
from TestData import data

if __name__ == "__main__":
    helper = Helper()
    browser = helper.browser()

    try:
        main_page = LetsKodeitMainPage(browser)
        login_page = LetsKodeitLoginPage(browser)

        helper.navigate_to_page(browser)

        main_page.get_element_attribute(data.file_name)

        main_page.save_alert_text_to_file(data.file_name)

        main_page.hover_and_click_top()

        main_page.write_footer_text(data.file_name)

        login_page.login_with_invalid_data(data.username, data.password, data.file_name)

        login_page.open_google_in_new_tab()

        print("Թեստը հաջողությամբ ավարտվեց:")

    except Exception as error:
        print(f"Թեստի ընթացքում տեղի ունեցավ սխալ: {error}")

    finally:
        helper.close_browser(browser)
