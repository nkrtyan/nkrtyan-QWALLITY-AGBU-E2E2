from selenium import webdriver
from selenium.webdriver.common.by import By



def test_visibility():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open Visibility page
        driver.get("http://www.uitestingplayground.com/visibility")

        # 1. Hide button
        try:
            hide_button = driver.find_element(By.ID, "hideButton")
            hide_button.click()
            print("Hide: PASSED - Hide button was clicked")

        except Exception as e:
            print(f"Hide: FAILED - {e}")


        # 2. Removed
        try:
            driver.find_element(By.ID, "removedButton")
            print("Removed: FAILED - button still exists")

        except:
            print("Removed: PASSED - button was removed")


        # 3. Zero Width
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

        except Exception as e:
            print(f"Zero Width: FAILED - {e}")


        # 4. Overlapped
        try:
            overlapped = driver.find_element(
                By.ID, "overlappedButton"
            )

            if overlapped.is_displayed():
                print(
                    "Overlapped: PASSED - "
                    "button exists but is overlapped"
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
            opacity_button = driver.find_element(
                By.ID, "transparentButton"
            )

            opacity = opacity_button.value_of_css_property(
                "opacity"
            )

            if opacity == "0":
                print("Opacity 0: PASSED - opacity is 0")
            else:
                print(
                    f"Opacity 0: FAILED - opacity is {opacity}"
                )

        except Exception as e:
            print(f"Opacity 0: FAILED - {e}")


        # 6. Visibility Hidden
        try:
            visibility_button = driver.find_element(
                By.ID, "invisibleButton"
            )

            visibility = visibility_button.value_of_css_property(
                "visibility"
            )

            if visibility == "hidden":
                print(
                    "Visibility Hidden: PASSED - "
                    "visibility is hidden"
                )
            else:
                print(
                    f"Visibility Hidden: FAILED - "
                    f"visibility is {visibility}"
                )

        except Exception as e:
            print(f"Visibility Hidden: FAILED - {e}")


        # 7. Display None
        try:
            display_button = driver.find_element(
                By.ID, "notDisplayedButton"
            )

            display = display_button.value_of_css_property(
                "display"
            )

            if display == "none":
                print(
                    "Display None: PASSED - "
                    "display is none"
                )
            else:
                print(
                    f"Display None: FAILED - "
                    f"display is {display}"
                )

        except:
            print(
                "Display None: PASSED - "
                "button is not displayed"
            )


        # 8. Offscreen
        try:
            offscreen = driver.find_element(
                By.ID, "offscreenButton"
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