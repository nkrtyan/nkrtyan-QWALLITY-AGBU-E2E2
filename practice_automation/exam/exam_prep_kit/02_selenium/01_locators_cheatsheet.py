"""
SELENIUM LOCATORS CHEAT SHEET
================================
Locators are how you find an element on a page before interacting with it.
Every command below assumes you already have a `driver` (WebDriver instance).

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
"""

# ---------------------------------------------------------------------------
# 1. THE 8 LOCATOR STRATEGIES (`By` class)
# ---------------------------------------------------------------------------
# By.ID                 -> unique id attribute (fastest, most reliable — prefer this first)
# By.NAME                -> name attribute
# By.CLASS_NAME           -> a single CSS class
# By.TAG_NAME             -> HTML tag, e.g. "input", "a"
# By.LINK_TEXT             -> exact visible text of an <a> link
# By.PARTIAL_LINK_TEXT      -> partial visible text of an <a> link
# By.CSS_SELECTOR            -> CSS selector pattern (recommended when no id/name)
# By.XPATH                    -> XML path expression (most powerful, most flexible)

# find_element() -> returns the FIRST matching element, raises NoSuchElementException if none found
# find_elements() -> returns a LIST of all matching elements (empty list if none found, no error)

# element = driver.find_element(By.ID, "email")
# elements = driver.find_elements(By.CLASS_NAME, "product-card")

# Priority order to prefer, when multiple locators could work:
#   1. ID  2. NAME  3. CSS_SELECTOR  4. XPATH  (CSS is generally faster than XPath)


# ---------------------------------------------------------------------------
# 2. CSS SELECTOR — cheat sheet
# ---------------------------------------------------------------------------
# Tag & ID:              css=input#email
# Tag & Class:            css=input.inputtext
# Tag & Attribute:         css=input[name='lastName']
# Tag, Class & Attribute:   css=input.inputtext[tabindex="2"]
#
# Building blocks:
#   #idValue                 -> element with this ID
#   .className                -> element with this class
#   .className > childNode     -> DIRECT child only
#   .className childNode        -> any descendant (not just direct child)
#   .className > child:nth-of-type(n)  -> nth child of a given type
#
# Sub-string attribute matches:
#   [attr^='value']    -> attribute STARTS WITH value
#   [attr$='value']    -> attribute ENDS WITH value
#   [attr*='value']    -> attribute CONTAINS value
#
# Selenium usage examples:
#   driver.find_element(By.CSS_SELECTOR, "input[id^='Em']")   # id starts with "Em"
#   driver.find_element(By.CSS_SELECTOR, "input[id$='001']")  # id ends with "001"
#   driver.find_element(By.CSS_SELECTOR, "input[id*='id']")   # id contains "id"


# ---------------------------------------------------------------------------
# 3. XPATH — cheat sheet
# ---------------------------------------------------------------------------
# Basic syntax: //tagname[@attribute='value']
#
# Selector | Meaning
# ---------|----------------------------------------------------------------
# nodename | selects all nodes with this name
# /        | selects from the root node    -> ABSOLUTE path (fragile: breaks if page layout changes)
# //       | selects nodes anywhere in the doc -> RELATIVE path (preferred, more robust)
# @        | selects an attribute
# *        | matches any element
# @*       | matches any attribute
# |        | OR — combine several paths
#
# Basic: //input[@name='uid']
#
# contains() — find element by PARTIAL text/attribute match:
#   //*[contains(text(),'message')]
#
# starts-with() — useful when attribute values change dynamically (e.g. auto-generated ids):
#   //label[starts-with(@id,'message')]
#
# text() — find element by its EXACT visible text:
#   //td[text()='UserID']
#
# Combine conditions with AND / OR:
#   //*[@type='submit' or @name='btnReset']
#   //*[@type='submit' and @name='btnLogin']


# ---------------------------------------------------------------------------
# 4. XPATH AXES — navigating relative to the current node
# ---------------------------------------------------------------------------
# Axis              | Result
# ------------------|-----------------------------------------------------
# ancestor           | all ancestors (parent, grandparent, ...) of current node
# descendant          | all descendants (children, grandchildren, ...)
# following            | all nodes AFTER the current node in the document
# preceding             | all nodes BEFORE the current node in the document
# following-sibling      | siblings that come after the current node
# preceding-sibling        | siblings that come before the current node
# child                     | direct children of the current node
# parent                     | direct parent of the current node
#
# Examples:
#   //*[@type='text']/following::input
#   //*[@type='submit']/following-sibling::input
#   //*[@type='submit']/preceding::input
#   //*[text()='Enterprise Testing']/ancestor::div
#   //*[@type='submit']/parent::div
#   //*[@id='java_technologies']/child::li[1]


# ---------------------------------------------------------------------------
# 5. XPATH vs CSS SELECTOR — know the trade-offs
# ---------------------------------------------------------------------------
# XPath:
#   + can traverse BOTH directions (parent<->child, i.e. bidirectional)
#   + can select by visible TEXT via text()
#   - generally slower than CSS
#   Syntax: //tagname[@attribute='value']
#
# CSS Selector:
#   + faster / better performance than XPath
#   - can only traverse parent -> child (one direction)
#   - cannot select by visible text
#   Syntax: tagname[attribute='value']


# ---------------------------------------------------------------------------
# 6. FULL WORKED EXAMPLES
# ---------------------------------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

# By ID
driver.find_element(By.ID, "name")

# By CSS, tag + attribute
driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")

# By CSS, "starts with"
driver.find_element(By.CSS_SELECTOR, "input[id^='Em']")

# By XPath, exact text
driver.find_element(By.XPATH, "//td[text()='UserID']")

# By XPath, contains partial text
driver.find_element(By.XPATH, "//*[contains(text(),'message')]")

# By XPath axis, find the input following a specific text field
driver.find_element(By.XPATH, "//*[@type='text']/following::input")

driver.quit()
"""
