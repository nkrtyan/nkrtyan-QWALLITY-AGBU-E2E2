"""
SELENIUM WEBDRIVER COMMANDS CHEAT SHEET
==========================================
Command categories: Navigation, Browser, Get, WebElement, Action/Result.
Assumes:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
"""

# ---------------------------------------------------------------------------
# 1. NAVIGATION COMMANDS
# ---------------------------------------------------------------------------
# driver.get("https://example.com")   # load a URL in the current window
# driver.back()                        # browser back button
# driver.forward()                     # browser forward button
# driver.refresh()                     # reload current page


# ---------------------------------------------------------------------------
# 2. BROWSER COMMANDS
# ---------------------------------------------------------------------------
# driver.title              # get the page title      (property, no parentheses)
# driver.current_url        # get the current URL      (property, no parentheses)
#
# Good practice: always close the browser window(s) opened by your test.
# driver.close()   # closes the CURRENT window only
# driver.quit()    # closes ALL windows AND ends the WebDriver session (use at test teardown)


# ---------------------------------------------------------------------------
# 3. WEBELEMENT COMMANDS — locate, then interact
# ---------------------------------------------------------------------------
# You must LOCATE an element before you can interact with it.
# element = driver.find_element(By.ID, "any_id")
# elements = driver.find_elements(By.NAME, "any_name")   # plural -> list of matches

# Type text into an input field
# driver.find_element(By.ID, "any_id").send_keys("some text")

# Clear an input field before typing (important! send_keys APPENDS, doesn't overwrite)
# element = driver.find_element(By.NAME, "any_name")
# element.clear()
# element.send_keys("new text")

# Click an element
# driver.find_element(By.ID, "any_id").click()

# Common HTML attributes you'll often need to check with get_attribute():
#   alt, disabled, href, id, src, style, title
# element.get_attribute("id")
# element.get_attribute("href")


# ---------------------------------------------------------------------------
# 4. GET COMMANDS — reading values back from an element
# ---------------------------------------------------------------------------
# driver.find_element(By.ID, "any_id").text          # visible TEXT content of an element


# ---------------------------------------------------------------------------
# 5. ELEMENT STATE CHECKS (WebElement methods, return True/False)
# ---------------------------------------------------------------------------
# element.is_displayed()   # is it visible on the page?
# element.is_enabled()     # is it enabled (clickable) or disabled?
# element.is_selected()    # is it selected (checkboxes, radio buttons, options)?


# ---------------------------------------------------------------------------
# 6. DROPDOWN / SELECT LISTS — needs the Select class
# ---------------------------------------------------------------------------
"""
from selenium.webdriver.support.ui import Select

select_element = Select(driver.find_element(By.ID, "carselect"))
select_element.select_by_index(2)              # 0-based index
select_element.select_by_value("honda")         # by the <option value="honda">
select_element.select_by_visible_text("Benz")   # by the text shown to the user

select_element.deselect_all()   # only works on MULTI-select dropdowns
"""


# ---------------------------------------------------------------------------
# 7. WORKING WITH WINDOWS / TABS
# ---------------------------------------------------------------------------
"""
driver.execute_script("window.open('')")   # open a new blank tab

before = driver.window_handles[0]   # handle of the original tab
after = driver.window_handles[1]    # handle of the new tab

driver.switch_to.window(after)      # switch focus to the new tab
driver.get("https://www.python.org/")
print(driver.title)

driver.switch_to.window(before)     # switch back to the original tab
print(driver.title)

driver.quit()
"""


# ---------------------------------------------------------------------------
# 8. MOUSE OPERATIONS — hover, scroll (ActionChains)
# ---------------------------------------------------------------------------
"""
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "carselect")
actions = ActionChains(driver)
actions.move_to_element(element).perform()   # hover over an element

# Scroll an element into view (via JavaScript)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
"""


# ---------------------------------------------------------------------------
# 9. WORKING WITH FRAMES / IFRAMES
# ---------------------------------------------------------------------------
# You MUST switch into a frame before interacting with elements inside it.
"""
driver.switch_to.frame("frame_id_or_name")            # switch by id/name
driver.switch_to.frame(driver.find_element(By.ID, "myframe"))  # switch by located element
driver.switch_to.default_content()                    # switch back to the main page
"""


# ---------------------------------------------------------------------------
# 10. WORKING WITH ALERTS / POPUPS
# ---------------------------------------------------------------------------
"""
alert = driver.switch_to.alert   # must switch to the alert before interacting with it
print(alert.text)                 # read the alert's message
alert.send_keys("some input")     # type into a PROMPT alert (only works if it has an input box)
alert.accept()                    # click OK
alert.dismiss()                   # click Cancel
"""


# ---------------------------------------------------------------------------
# 11. SCREENSHOTS & WINDOW SIZE
# ---------------------------------------------------------------------------
# driver.maximize_window()
# driver.fullscreen_window()
# driver.set_window_size(1024, 768)
# driver.save_screenshot("screenshot.png")   # give a path, or it saves in the current dir
