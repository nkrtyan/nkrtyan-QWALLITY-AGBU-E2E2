from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.uitestingplayground.com")


hide_button = (By.XPATH, '//button[text()="HideButtons()"]')
removed_buttonn = (By.XPATH, '//button[text()="Removed"]')
zero_button = (By.XPATH, '//button[text() = "Zero Width"]')
overlapped_button =(By.XPATH, '//button[text() = "Overlapped"]')
opacity_button = (By.XPATH, '//*[@id="transparentButton"]')
visibiltyhidden_button = (By.XPATH, '//*[@id="invisibleButton"]')
displaynone_button = (By.XPATH, '//*[@id="invisibleButton"]')
offscreen_button = (By.XPATH, '//*[@id="offscreenButton"]')



def test_visibility(driver):
    driver.get("https://www.uitestingplayground.com/visibility")

    hide_button = driver.find_element(By.ID, "hideButton")
    hide_button.click()

    removed_buttons = driver.find_elements(By.ID, "removedButton")

    if len(removed_buttons) == 0:
        print("removedButton is hidden/removed")

    else:
        print("removedButton is still present")











from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_visibility(driver):
    driver.get("https://www.uitestingplayground.com/visibility")

    hide_button = driver.find_element(By.ID, "hideButton")
    hide_button.click()






    print("Zero width:", zero_width_button.is_displayed())
    print("Transparent:", transparent_button.is_displayed())
    print("Invisible:", invisible_button.is_displayed())
    print("Not displayed:", not_displayed_button.is_displayed())
    print("Offscreen:", offscreen_button.is_displayed())



def test_progress_bar(driver):
    driver.get("https://www.uitestingplayground.com/progressbar")

    start_button = driver.find_element(By.ID, "startButton")
    stop_button = driver.find_element(By.ID, "stopButton")

    start_time = time.time()

    start_button.click()

    time.sleep(2)

    stop_button.click()

    duration = time.time() - start_time

    print("Duration:", duration, "seconds")



def test_text_input(driver):
    driver.get("https://www.uitestingplayground.com/textinput")

    text = "Hello Selenium"

    input_field = driver.find_element(By.ID, "newButtonName")
    button = driver.find_element(By.ID, "updatingButton")

    input_field.send_keys(text)

    button.click()

    button_text = button.text

    print("Entered text:", text)
    print("Button text:", button_text)

    assert button_text == text

    print("Text input test passed!")



def main():
    driver = webdriver.Chrome()

    test_visibility(driver)
    test_progress_bar(driver)
    test_text_input(driver)

    driver.quit()



if __name__ == "__main__":
    main()
Jot something down




from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_visibility(driver):
    # Open Visibility page
    driver.get("https://www.uitestingplayground.com/visibility")

    # Find and click Hide button
    hide_button = driver.find_element(By.ID, "hideButton")
    hide_button.click()

    time.sleep(1)

    # List of buttons that should become hidden
    buttons = [
    "removedButton",
    "zeroWidthButton",
    "overlappedButton",
    "transparentButton",
    "invisibleButton",
    "notdisplayedButton",
    "offscreenButton"
    ]

    # Check visibility of each button
    for button_id in buttons:
        button = driver.find_element(By.ID, button_id)

    if not button.is_displayed():
        print(f"{button_id}: Hidden")

    else:
        print(f"{button_id}: Visible")



def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        test_visibility(driver)
    finally:
        time.sleep(2)
        driver.quit()



if __name__ == "__main__":
    main()








from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_driver = webdriver.Chrome()
my_driver.maximize_window()
my_driver.get("http://www.uitestingplayground.com/")
visibility_lokator = my_driver.find_element(By.XPATH, '//a[text()="Visibility"]')
visibility_lokator.click()

removed_btn =(By.XPATH, '//button[text()="Removed"]')
zero_btn = (By.XPATH, '//button[text() = "Zero Width"]')
overlapped_btn =(By.XPATH, '//button[text() = "Overlapped"]')
opacity_button = (By.XPATH, '//*[@id="transparentButton"]')
visibiltyhidden_button = (By.XPATH, '//*[@id="invisibleButton"]')
displaynone_button = (By.XPATH, '//*[@id="invisibleButton"]')
offscreen_button = (By.XPATH, '//*[@id="offscreenButton"]')



btn_list = [removed_btn, zero_btn, overlapped_btn, opacity_button, visibiltyhidden_button, displaynone_button, offscreen_button]

hide_button = my_driver.find_element(By.XPATH, '//button[text()="Hide"]')
hide_button.click()

def check_list(btn_list):
    for i in btn_list:

        try:
            if not overlapped_div.is_displayed():
                print("Overlapped div disappeared")
    else:
        print("Overlapped div is still displayed")

    if not my_driver.find_element(*i).is_displayed():
        print(f"{i} is hidden")
    else:
        print(f"{i} is not hidden")

    except:
    
    print(f"{i} button is hidden")





if __name__=="__main__":
    check_list(btn_list)






from selenium import webdriver
from selenium.webdriver.common.by import By


def test_visibility():
    driver = webdriver.Chrome()

    try:
        # Open Visibility page
        driver.get("http://www.uitestingplayground.com/visibility")

        # Locators
        hide_button = (By.XPATH, '//button[text()="Hide"]')
        removed_btn = (By.XPATH, '//button[text()="Removed"]')
        zero_btn = (By.XPATH, '//button[text()="Zero Width"]')
        overlapped_btn = (By.XPATH, '//button[text()="Overlapped"]')
        opacity_button = (By.XPATH, '//*[@id="transparentButton"]')
        visibilityhidden_button = (By.XPATH, '//*[@id="invisibleButton"]')
        displaynone_button = (By.XPATH, '//*[@id="notDisplayedButton"]')
        offscreen_button = (By.XPATH, '//*[@id="offscreenButton"]')

        # 1. Hide
        try:
            hide = driver.find_element(*hide_button)
            hide.click()
            print("Hide: PASSED")

        except Exception as e:
            print(f"Hide: FAILED - {e}")


        # 2. Removed
        try:
            driver.find_element(*removed_btn)
            print("Removed: FAILED - button still exists")

        except:
            print("Removed: PASSED - button was removed")


        # 3. Zero Width
        try:
            zero = driver.find_element(*zero_btn)

            width = zero.size["width"]

            if width == 0:
                print("Zero Width: PASSED - width is 0")
            else:
                print(f"Zero Width: FAILED - width is {width}")

        except Exception as e:
            print(f"Zero Width: FAILED - {e}")


        # 4. Overlapped
        try:
            overlapped = driver.find_element(*overlapped_btn)

            if overlapped.is_displayed():
                print(
                    "Overlapped: PASSED - "
                    "button still exists"
                )
            else:
                print(
                    "Overlapped: FAILED - "
                    "button is not displayed"
                )

        except Exception as e:
            print(f"Overlapped: FAILED - {e}")


        # 5. Opacity 0
        try:
            opacity = driver.find_element(*opacity_button)

            value = opacity.value_of_css_property("opacity")

            if value == "0":
                print("Opacity 0: PASSED - opacity is 0")
            else:
                print(
                    f"Opacity 0: FAILED - opacity is {value}"
                )

        except Exception as e:
            print(f"Opacity 0: FAILED - {e}")


        # 6. Visibility Hidden
        try:
            visibility = driver.find_element(
                *visibilityhidden_button
            )

            value = visibility.value_of_css_property(
                "visibility"
            )

            if value == "hidden":
                print(
                    "Visibility Hidden: PASSED - "
                    "visibility is hidden"
                )
            else:
                print(
                    f"Visibility Hidden: FAILED - "
                    f"visibility is {value}"
                )

        except Exception as e:
            print(
                f"Visibility Hidden: FAILED - {e}"
            )


        # 7. Display None
        try:
            display_none = driver.find_element(
                *displaynone_button
            )

            value = display_none.value_of_css_property(
                "display"
            )

            if value == "none":
                print(
                    "Display None: PASSED - "
                    "display is none"
                )
            else:
                print(
                    f"Display None: FAILED - "
                    f"display is {value}"
                )

        except:
            print(
                "Display None: PASSED - "
                "button is not displayed"
            )


        # 8. Offscreen
        try:
            offscreen = driver.find_element(
                *offscreen_button
            )

            location = offscreen.location

            if location["x"] < 0 or location["y"] < 0:
                print(
                    "Offscreen: PASSED - "
                    "button is outside the screen"
                )
            else:
                print(
                    "Offscreen: FAILED - "
                    "button is still on screen"
                )

        except Exception as e:
            print(f"Offscreen: FAILED - {e}")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_visibility()



from selenium import webdriver
from selenium.webdriver.common.by import By


def check_list(driver, btn_list):

    for button in btn_list:

        try:
            element = driver.find_element(*button)

            if not element.is_displayed():
                print(f"{button} is hidden")
            else:
                print(f"{button} is still displayed")

        except:
            print(f"{button} button is hidden or removed")


def main():

    my_driver = webdriver.Chrome()
    my_driver.maximize_window()

    try:
        # Open website
        my_driver.get("http://www.uitestingplayground.com/")

        # Open Visibility page
        visibility_locator = (
            By.XPATH, '//a[text()="Visibility"]'
        )

        visibility_link = my_driver.find_element(
            *visibility_locator
        )

        visibility_link.click()

        # Locators
        removed_btn = (
            By.XPATH, '//button[text()="Removed"]'
        )

        zero_btn = (
            By.XPATH, '//button[text()="Zero Width"]'
        )

        overlapped_btn = (
            By.XPATH, '//button[text()="Overlapped"]'
        )

        opacity_button = (
            By.XPATH, '//*[@id="transparentButton"]'
        )

        visibilityhidden_button = (
            By.XPATH, '//*[@id="invisibleButton"]'
        )

        displaynone_button = (
            By.XPATH, '//*[@id="notDisplayedButton"]'
        )

        offscreen_button = (
            By.XPATH, '//*[@id="offscreenButton"]'
        )

        # Put buttons into list
        btn_list = [
            removed_btn,
            zero_btn,
            overlapped_btn,
            opacity_button,
            visibilityhidden_button,
            displaynone_button,
            offscreen_button
        ]

        # Find Hide button
        hide_button = my_driver.find_element(
            By.XPATH, '//button[text()="Hide"]'
        )

        # Click Hide
        hide_button.click()

        # Check buttons
        check_list(my_driver, btn_list)

    finally:
        my_driver.quit()


if __name__ == "__main__":
    main()