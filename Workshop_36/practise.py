from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_visibility(driver):
    driver.get("https://www.uitestingplayground.com/visibility")

    # 1. Find Hide button
    hide_button = driver.find_element(By.ID, "hideButton")

    # 2. Click Hide button
    hide_button.click()

    # 3. Check Removed button
    removed_button = driver.find_elements(By.ID, "removedButton")

    print("Removed:", len(removed_button) > 0)

    # 4. Find other buttons
    zero_width_button = driver.find_element(By.ID, "zeroWidthButton")
    overlapped_button = driver.find_element(By.ID, "overlappedButton")
    transparent_button = driver.find_element(By.ID, "transparentButton")
    invisible_button = driver.find_element(By.ID, "invisibleButton")
    not_displayed_button = driver.find_element(By.ID, "notdisplayedButton")
    offscreen_button = driver.find_element(By.ID, "offscreenButton")

    # 5. Check visibility
    print("Zero width:", zero_width_button.is_displayed())
    print("Overlapped:", overlapped_button.is_displayed())
    print("Transparent:", transparent_button.is_displayed())
    print("Invisible:", invisible_button.is_displayed())
    print("Not displayed:", not_displayed_button.is_displayed())
    print("Offscreen:", offscreen_button.is_displayed())




def test_progress_bar(driver):
    driver.get("https://www.uitestingplayground.com/progressbar")

    # Find Start button
    start_button = driver.find_element(By.ID, "startButton")

    # Find Stop button
    stop_button = driver.find_element(By.ID, "stopButton")

    # Start timer
    start_time = time.time()

    # Start progress bar
    start_button.click()

    # Wait 2 seconds
    time.sleep(2)

    # Stop progress bar
    stop_button.click()

    # Calculate duration
    duration = time.time() - start_time

    print("Duration:", duration, "seconds")



def test_text_input(driver):
    driver.get("https://www.uitestingplayground.com/textinput")

    # Text that we want to enter
text = "Hello Selenium"

    # Find input field
input_field = driver.find_element(By.ID, "newButtonName")

    # Find button
button = driver.find_element(By.ID, "updatingButton")

    # Enter text
input_field.send_keys(text)

    # Click button
button.click()

    # Get button text
button_text = button.text

print("Entered text:", text)
print("Button text:", button_text)

    # Verify result
assert button_text == text

print("Text input test passed!")




def main():
    # Create Chrome browser
    driver = webdriver.Chrome()


try:
    # Run Visibility test
        test_visibility(driver)

    # Run Progress Bar test
        test_progress_bar(driver)

    # Run Text Input test
        test_text_input(driver)

finally:
    # Close browser
    driver.quit()





if __name__ == "__main__":
    main()





from selenium import webdriver
from selenium.webdriver.common.by import By


def test_visibility():
    driver = webdriver.Chrome()

    try:
        # Open Visibility page
        driver.get("http://www.uitestingplayground.com/visibility")

        # Find Hide button and click it
        hide_button = driver.find_element(By.ID, "hideButton")
        hide_button.click()

        # Check that buttons are hidden
        removed_button = driver.find_element(By.ID, "removedButton")
        zero_width_button = driver.find_element(By.ID, "zeroWidthButton")
        transparent_button = driver.find_element(By.ID, "transparentButton")

        if not removed_button.is_displayed():
            print("Removed button is hidden")
        else:
            print("Removed button is visible")

        if not zero_width_button.is_displayed():
            print("Zero width button is hidden")
        else:
            print("Zero width button is visible")

        if not transparent_button.is_displayed():
            print("Transparent button is hidden")
        else:
            print("Transparent button is visible")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_visibility()



from selenium import webdriver
from selenium.webdriver.common.by import By


def test_visibility():
    driver = webdriver.Chrome()

    try:
        # 1. Open Visibility page
        driver.get("http://www.uitestingplayground.com/visibility")

        # 2. Find and click Hide button
        hide_button = driver.find_element(By.ID, "hideButton")
        hide_button.click()

        # ---------------------------------------
        # 2. Removed
        # ---------------------------------------
        try:
            driver.find_element(By.ID, "removedButton")
            print("Removed: FAILED - element still exists")

        except:
            print("Removed: PASSED - element was removed")


        # ---------------------------------------
        # 3. Zero Width
        # ---------------------------------------
        try:
            zero_width = driver.find_element(
                By.ID, "zeroWidthButton"
            )

            width = zero_width.size["width"]

            if width == 0:
                print("Zero Width: PASSED - width is 0")
            else:
                print(
                    f"Zero Width: FAILED - width is {width}"
                )

        except:
            print("Zero Width: FAILED - element not found")


        # ---------------------------------------
        # 4. Overlapped
        # ---------------------------------------
        try:
            overlapped = driver.find_element(
                By.ID, "overlappedButton"
            )

            is_overlapped = driver.execute_script("""
                const element = arguments[0];
                const rect = element.getBoundingClientRect();

                const x = rect.left + rect.width / 2;
                const y = rect.top + rect.height / 2;

                const topElement = document.elementFromPoint(x, y);

                return topElement !== element &&
                       !element.contains(topElement);
            """, overlapped)

            if is_overlapped:
                print("Overlapped: PASSED - element is covered")
            else:
                print("Overlapped: FAILED - element is not covered")

        except:
            print("Overlapped: FAILED - element not found")


        # ---------------------------------------
        # 5. Opacity 0
        # ---------------------------------------
        try:
            opacity = driver.find_element(
                By.ID, "transparentButton"
            )

            value = opacity.value_of_css_property("opacity")

            if value == "0":
                print("Opacity 0: PASSED - opacity is 0")
            else:
                print(
                    f"Opacity 0: FAILED - opacity is {value}"
                )

        except:
            print("Opacity 0: FAILED - element not found")


        # ---------------------------------------
        # 6. Visibility Hidden
        # ---------------------------------------
        try:
            visibility = driver.find_element(
                By.ID, "invisibleButton"
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

        except:
            print(
                "Visibility Hidden: FAILED - "
                "element not found"
            )


        # ---------------------------------------
        # 7. Display None
        # ---------------------------------------
        try:
            display_none = driver.find_element(
                By.ID, "notDisplayedButton"
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
                "element is not displayed"
            )


        # ---------------------------------------
        # 8. Offscreen
        # ---------------------------------------
        try:
            offscreen = driver.find_element(
                By.ID, "offscreenButton"
            )

            location = offscreen.location

            if location["x"] < 0 or location["y"] < 0:
                print(
                    "Offscreen: PASSED - "
                    "element is outside the screen"
                )
            else:
                print(
                    "Offscreen: FAILED - "
                    "element is still on screen"
                )

        except:
            print("Offscreen: FAILED - element not found")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_visibility()