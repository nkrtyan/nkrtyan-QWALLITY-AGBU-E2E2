from helpers.screenshot_helper import ScreenshotHelper


class TestHelper:

    @staticmethod
    def screenshot(driver, name):
        ScreenshotHelper.take_screenshot(driver, name)

    @staticmethod
    def save_text(title, text, mode="a"):
        with open("live_coding_text.txt", mode, encoding="utf-8") as file:
            file.write(title + "\n")
            file.write(str(text) + "\n\n")

    @staticmethod
    def wrong_login(login_page, email, password):
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
        return login_page.get_error_message()

    @staticmethod
    def open_google(driver, url):
        driver.switch_to.new_window("tab")
        driver.get(url)