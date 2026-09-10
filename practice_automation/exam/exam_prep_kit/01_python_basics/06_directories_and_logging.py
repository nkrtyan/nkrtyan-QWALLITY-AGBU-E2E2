"""
DIRECTORIES & LOGGING CHEAT SHEET
====================================
The `os` module for working with paths/folders, and the `logging` module
for proper logging (much better than scattering print() statements —
this is exactly what Selenium test frameworks use to record what happened).
"""

import os
import shutil
import logging

# ---------------------------------------------------------------------------
# 1. THE `os` MODULE — paths & directories
# ---------------------------------------------------------------------------
print(os.getcwd())                        # current working directory (where script runs from)
print(os.path.abspath(__file__))           # absolute path of THIS script file
print(os.path.abspath("myfolder/myfile.txt"))  # turn a relative path into an absolute one

if os.path.isdir("some_directory"):
    print("It is a directory")

if os.path.exists("some_directory"):       # check existence BEFORE creating, to avoid errors
    print("some_directory already exists")

os.path.join("my_directory", "my_file.txt")  # build a path safely (handles / vs \ per-OS)
# ALWAYS prefer os.path.join() over manually concatenating strings with "/" or "\\"

# Creating / removing directories
# os.mkdir("newdir")            # create ONE new directory (errors if parent path missing)
# os.makedirs("a/b/c")          # create nested directories, ALL levels at once
# os.rmdir("newdir")            # remove an EMPTY directory only
# shutil.rmtree("newdir")       # remove a directory AND everything inside it (be careful!)

# Renaming / removing files
# os.rename("a.txt", "c.txt")
# os.remove("file.txt")         # delete a single file (not a directory)

# os.chdir("newdir")            # change the current working directory


# ---------------------------------------------------------------------------
# 2. PUTTING IT TOGETHER — classic exam-style task
# ---------------------------------------------------------------------------
def create_directory_and_append_text(directory_name, file_name, text):
    """Create a directory (if missing), then append text to a file inside it."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)          # note: os.makedirs, not os.mkdirs (common typo!)

    file_path = os.path.join(directory_name, file_name)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print(f"Text appended to {file_path}")


def cleanup(directory_name):
    """Remove a directory and everything inside it."""
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
        print(f"Directory '{directory_name}' and all its contents have been removed.")


# Example usage:
# create_directory_and_append_text("my_directory", "my_file.txt", "This is a new line of text.")
# cleanup("my_directory")


# ---------------------------------------------------------------------------
# 3. LOGGING — levels, from least to most severe
# ---------------------------------------------------------------------------
# Level    | When to use it
# ---------|---------------------------------------------------------------
# DEBUG    | Detailed info, useful only when diagnosing problems
# INFO     | Confirmation that things are working as expected
# WARNING  | Something unexpected happened, but the program still works
# ERROR    | A more serious problem — some function failed
# CRITICAL | A serious error — the program itself may be unable to continue

# basicConfig() sets up logging ONCE, ideally at the top of your main script/module.
logging.basicConfig(
    level=logging.DEBUG,                                  # show DEBUG and everything above it
    format="%(asctime)s [%(levelname)s] %(message)s",     # what each log line looks like
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="my_log.log",   # if omitted, logs print to console instead of a file
    filemode="a",             # 'a' = append to existing log, 'w' = overwrite each run
    encoding="utf-8",
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# IMPORTANT: level=logging.DEBUG means "show DEBUG and everything more severe".
# If you set level=logging.WARNING instead, DEBUG and INFO messages get silently
# ignored — a common exam gotcha ("why isn't my debug message showing up?").

# Example output line:
# 2023-10-25 15:30:00 [DEBUG] This is a debug message


# ---------------------------------------------------------------------------
# 4. USING LOGGING ACROSS MULTIPLE FILES (a "logging config" module)
# ---------------------------------------------------------------------------
# logging_config.py:
#     import logging
#     logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
#
# second_module.py:
#     import logging_config     # runs the basicConfig() setup once, on import
#     import logging
#     logging.info("This is a new message")   # uses the shared configuration
