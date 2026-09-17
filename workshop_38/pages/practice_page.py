from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticePage:

    
    # Locators
    

    ALERT_BUTTON = (
        By.ID,
        "alertbtn"
    )

    HIDE_BUTTON = (
        By.ID,
        "hide-textbox"
    )

    TEXTBOX = (
        By.ID,
        "displayed-text"
    )

    MOUSE_HOVER = (
        By.ID,
        "mousehover"
    )

    TOP_OPTION = (
        By.XPATH,
        "//a[text()='Top']"
    )

    FOOTER = (
        By.TAG_NAME,
        "footer"
    )

    SIGN_IN = (
        By.XPATH,
        "//a[contains(@href, '/login')]"
    )

    
    # Constructor
    

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )


    # Alert
    

    def click_alert(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.ALERT_BUTTON
            )
        ).click()

    def get_alert_text(self):

        alert = self.wait.until(
            EC.alert_is_present()
        )

        return alert.text

    def accept_alert(self):

        self.driver.switch_to.alert.accept()

   
    # Hide element
    

    def hide_textbox(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.HIDE_BUTTON
            )
        ).click()

    def get_textbox_attribute(self):

        textbox = self.driver.find_element(
            *self.TEXTBOX
        )

        return textbox.get_attribute(
            "style"
        )

    
    # Mouse Hover
    

    def move_to_mouse_hover(self):

        mouse_hover = self.wait.until(
            EC.visibility_of_element_located(
                self.MOUSE_HOVER
            )
        )

        ActionChains(
            self.driver
        ).move_to_element(
            mouse_hover
        ).perform()

    def click_top(self):

        top_option = self.wait.until(
            EC.element_to_be_clickable(
                self.TOP_OPTION
            )
        )

        top_option.click()

    
    # Footer
   

    def get_footer_text(self):

        footer = self.wait.until(
            EC.presence_of_element_located(
                self.FOOTER
            )
        )

        return footer.text

    
    # Sign In
    

    def click_sign_in(self):

        sign_in = self.wait.until(
            EC.presence_of_element_located(
                self.SIGN_IN
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            sign_in
        )

        self.driver.execute_script(
            "arguments[0].click();",
            sign_in
        )