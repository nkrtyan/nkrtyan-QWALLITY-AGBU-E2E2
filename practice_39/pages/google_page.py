from lib.helpers import Helper, error_handler
import config


class GooglePage(Helper):

    @error_handler
    def open_google_page(self):
        self.go_to_page(
            config.google_url,
            new_window=True
        )
        self.switch_window(1)

        self.test_logger.info(
            "Opened Google page"
        )