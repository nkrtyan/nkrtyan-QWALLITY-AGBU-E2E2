from lib.helpers import Helper
import config


class GooglePage(Helper):

    open_google = config.google_url

    def go_to_google(self):
        try:
            self.go_to_page(self.open_google, new_window=True)
            self.switch_window(1)
            self.test_logger.info('Google page opened')
        except Exception as e:
            self.test_logger.error(f'Google page opening failed: {e}')
            raise