# Selenium + Python UI Automation — Exam Prep Kit

A quick-reference folder built from your course slide decks. Each file is a
heavily commented, runnable `.py` file — no fluff, just syntax + short
explanations you can `Ctrl+F` during the exam.

## How to use this

- Every file works as a **standalone reference** — open it, search for the
  topic you need, copy the pattern.
- Comments explain the **"why"**, not just the "what" — especially around
  common gotchas (mutable vs immutable, implicit vs explicit waits, etc.).
- Runnable examples are left uncommented; full scripts that need a live
  browser/API are wrapped in triple-quoted strings so this file doesn't error
  out if you just run it top to bottom to sanity-check the syntax.

## Folder map

```
exam_prep_kit/
├── 01_python_basics/
│   ├── 01_collections.py                 # list, tuple, dict, set
│   ├── 02_decision_making_and_loops.py   # if/elif/else, for, while, break/continue/pass
│   ├── 03_functions_and_modules.py       # def, *args/**kwargs, scope, imports
│   ├── 04_oop_principles.py              # classes, encapsulation, inheritance, abstraction, polymorphism
│   ├── 05_file_io.py                     # open(), with, read/write, csv
│   └── 06_directories_and_logging.py     # os module, logging module
│
├── 02_selenium/
│   ├── 01_locators_cheatsheet.py         # By.ID/CSS/XPATH, CSS & XPath syntax, XPath axes
│   ├── 02_webdriver_commands.py          # navigation, element interaction, dropdowns, windows, alerts
│   ├── 03_waits_and_synchronization.py   # implicit vs explicit waits, expected_conditions
│   └── 04_full_worked_example.py         # a complete login test, script-style AND pytest-style
│
└── 03_bonus_rest_api/
    └── api_requests_example.py           # requests library: GET/POST/PUT/PATCH/DELETE, status codes
```

## If you only have 10 minutes before the exam, skim these in order

1. `02_selenium/01_locators_cheatsheet.py` — locators are the thing you'll
   use in nearly every question.
2. `02_selenium/03_waits_and_synchronization.py` — implicit vs explicit
   waits is a classic "explain the difference" question.
3. `02_selenium/02_webdriver_commands.py` — find_element vs find_elements,
   click/send_keys/get_attribute.
4. `01_python_basics/01_collections.py` — list slicing and dict iteration
   patterns show up constantly in "process this data" questions.
5. `01_python_basics/06_directories_and_logging.py` — logging levels
   (DEBUG < INFO < WARNING < ERROR < CRITICAL) and what `basicConfig(level=...)`
   actually filters.

## A couple of Python concepts worth knowing by name (came up implicitly in the course)

- **Context manager** (`with open(...) as f:`) — an object that defines
  what happens when you enter and leave a `with` block. For files, that
  means "open it" on entry and "close it automatically" on exit, even if
  an exception happens inside. pytest fixtures with `yield` work the same way.
- **`self`** — the first parameter of every instance method; it's how a
  method refers to the specific object it was called on.
- **`*args` / `**kwargs`** — catch-all parameters for "however many extra
  positional/keyword arguments the caller wants to pass."
- **Decorator** (e.g. `@abstractmethod`, `@pytest.fixture`) — a function
  that wraps another function/method to add behavior without changing its
  code. You don't need to write your own for this exam, but recognize the
  `@something` syntax above a `def`.

Good luck tomorrow!
