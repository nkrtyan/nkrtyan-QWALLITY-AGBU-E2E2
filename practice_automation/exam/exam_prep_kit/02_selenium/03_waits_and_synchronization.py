"""
SELENIUM WAITS CHEAT SHEET
=============================
Why waits matter: modern web apps load content asynchronously (AJAX). If your
script tries to interact with an element before it exists, you get a
NoSuchElementException or ElementNotInteractableException. Waits solve this.

There are two kinds: IMPLICIT and EXPLICIT. Know the difference — it's a
classic exam question.
"""

# ---------------------------------------------------------------------------
# 1. IMPLICIT WAIT — applies GLOBALLY, for the whole driver session
# ---------------------------------------------------------------------------
# Tells the driver: "whenever you search for an element and can't find it
# immediately, keep retrying for up to N seconds before giving up."
# Set it ONCE, right after creating the driver.
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)   # wait up to 10 seconds for ANY find_element() call
"""
# Downside: it's a blunt, one-size-fits-all timeout for every single lookup.


# ---------------------------------------------------------------------------
# 2. EXPLICIT WAIT — applies to ONE specific condition, at one specific point
# ---------------------------------------------------------------------------
# More precise: "wait up to N seconds for THIS specific condition to become true,
# then proceed (or raise TimeoutException if it never does)."
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10)   # max wait time = 10 seconds

# Most frequently used expected_conditions (EC):
element = wait.until(EC.presence_of_element_located((By.ID, "email")))
element = wait.until(EC.visibility_of_element_located((By.ID, "email")))
element = wait.until(EC.element_to_be_clickable((By.ID, "submit_btn")))
wait.until(EC.title_is("Dashboard"))
wait.until(EC.title_contains("Dashboard"))
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Success"))
wait.until(EC.alert_is_present())
wait.until_not(EC.visibility_of_element_located((By.ID, "loading_spinner")))  # wait for something to DISAPPEAR
"""

# Full list of other expected_conditions you may see referenced (less commonly used):
#   presence_of_all_elements_located, text_to_be_present_in_element_value,
#   frame_to_be_available_and_switch_to_it, invisibility_of_element_located,
#   element_to_be_selected, element_located_to_be_selected,
#   element_selection_state_to_be, element_located_selection_state_to_be


# ---------------------------------------------------------------------------
# 3. IMPLICIT vs EXPLICIT — quick comparison
# ---------------------------------------------------------------------------
# Implicit wait                          | Explicit wait
# ----------------------------------------|--------------------------------
# Set once, applies to the WHOLE driver    | Applied at a SPECIFIC point in the code
# Simple, but less flexible                 | More control, checks specific conditions
# "wait for element to exist" only          | Can wait for visibility, clickability,
#                                              text, title, alerts, etc.
#
# IMPORTANT: don't mix implicit and explicit waits carelessly in the same
# script — their timeouts can compound and cause confusing, inconsistent
# delays. Most teams pick ONE strategy (usually explicit waits) and stick to it.


# ---------------------------------------------------------------------------
# 4. PAGE LOAD TIMEOUT — a related but different setting
# ---------------------------------------------------------------------------
# Sets how long to wait for an entire PAGE to finish loading (not for a single
# element). Throws a TimeoutException if the page load takes too long.
# driver.set_page_load_timeout(30)


# ---------------------------------------------------------------------------
# 5. NEVER USE time.sleep() FOR SYNCHRONIZATION (anti-pattern, but you WILL
#    see it — know why it's bad for the exam)
# ---------------------------------------------------------------------------
# import time
# time.sleep(5)   # BAD: hardcoded, wastes time if the page loads faster,
#                  #      still fails if the page loads slower than 5s.
# Prefer explicit waits — they're both faster on average AND more reliable.
