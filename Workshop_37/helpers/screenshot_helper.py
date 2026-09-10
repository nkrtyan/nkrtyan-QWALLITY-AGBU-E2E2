from pathlib import Path


class ScreenshotHelper:

    def __init__(self, driver):
        self.driver = driver
        self.folder = Path(__file__).parent.parent / "screenshots"
        self.folder.mkdir(exist_ok=True)

    def take(self, name):
        path = self.folder / f"{name}.png"
        self.driver.save_screenshot(str(path))
        print(f"Screenshot saved: {path}")
