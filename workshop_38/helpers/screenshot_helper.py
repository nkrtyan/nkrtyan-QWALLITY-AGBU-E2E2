import os


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(driver, name):
        folder = "screenshots"

        if not os.path.exists(folder):
            os.makedirs(folder)

        path = os.path.join(folder, name)
        driver.save_screenshot(path)

        return path
