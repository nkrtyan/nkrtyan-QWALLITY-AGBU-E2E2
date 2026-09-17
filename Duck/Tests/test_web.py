from.Pages.search import DuckDuckGoSearchPage
from .Pages.result import DuckDuckGoResultPage
from Lib import Helper
from Duck.TestData import data
import time

if __name__ == "__main__":
    helper_obj = Helper()
    browser = helper_obj.my_browser()

    search_page = DuckDuckGoSearchPage(browser)
    helper_obj.navigate_to_page(browser)
    search_page.search(data.text)
    time.sleep(2)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0, "No result"
    assert result_page.search_input_value() == data.text, "Assertion failed, attribute data is incorrect"
    print(f"There are {result_page.link_div_count()} links in searched results.")

    helper_obj.close_browser(browser)
    print("Test completed successfully.")