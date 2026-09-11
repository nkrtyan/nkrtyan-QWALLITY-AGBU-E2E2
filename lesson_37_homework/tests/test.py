import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
#python -m tests.test  
from Helpers.lib import Helper
from pom.main import LetsKodeitMainPage
from pom.login import LetsKodeitLoginPage
from TestData import data, config

if __name__ == "__main__":
    helper = Helper()
    browser = helper.browser()

    main_page = LetsKodeitMainPage(browser)
    login_page = LetsKodeitLoginPage(browser)

    helper.navigate_to_page(browser)
    main_page.get_element_attribute(config.file_name)
    main_page.hover_and_click_top()
    main_page.get_footer_text(config.file_name)
    login_page.login(data.username, data.password, config.file_name)
    login_page.open_google_in_new_tab()
    print("Թեստը հաջողությամբ ավարտվեց:")

    browser.quit()
