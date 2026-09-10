"""
FILE INPUT / OUTPUT CHEAT SHEET
=================================
Reading and writing text files, CSVs, and Excel files.
"""

# ---------------------------------------------------------------------------
# 1. open() MODES — memorize this table
# ---------------------------------------------------------------------------
# Mode | Creates file if missing? | Effect
# -----|---------------------------|---------------------------------------
# "r"  | No  (errors if missing)  | Read only
# "w"  | Yes                       | Write — OVERWRITES/erases existing content
# "a"  | Yes                       | Append — adds to the end, keeps old content
# "r+" | No                        | Read + write
# "w+" | Yes                       | Read + write — OVERWRITES existing content
# "a+" | Yes                       | Read + append


# ---------------------------------------------------------------------------
# 2. THE `with` STATEMENT — always prefer this over manual open()/close()
# ---------------------------------------------------------------------------
# `with` is a CONTEXT MANAGER: it automatically closes the file for you, even
# if an error happens inside the block. Manual open()/close() risks leaving
# a file handle open if an exception is raised before you reach .close().
with open("test.txt", "w+", encoding="utf-8") as file:
    file.write("Hello new version")
# file is automatically closed here, as soon as the `with` block ends.

# The manual (not recommended) way, for comparison:
file = open("file_manual.txt", "w+", encoding="utf-8")
file.write("Hello\nWorld")
file.close()   # you MUST remember to call this yourself


# ---------------------------------------------------------------------------
# 3. READING FILES — read() vs readline() vs readlines()
# ---------------------------------------------------------------------------
with open("test.txt", "r", encoding="utf-8") as f:
    whole_thing = f.read()          # entire file as ONE string

with open("test.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()       # reads just ONE line (including its \n)
    second_line = f.readline()      # calling again reads the NEXT line

with open("test.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()       # returns a LIST of lines, each ending in \n

# Looping over a file line by line (memory-efficient, very common pattern)
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())         # .strip() removes the trailing \n and whitespace


# ---------------------------------------------------------------------------
# 4. WRITING FILES — write() vs writelines()
# ---------------------------------------------------------------------------
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")             # write() does NOT add \n automatically — add it yourself

lines_to_write = ["Line 1", "Line 2", "Line 3"]
with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(line + "\n" for line in lines_to_write)   # writelines needs \n per item too


# ---------------------------------------------------------------------------
# 5. APPENDING — "a" mode adds to the end without erasing existing content
# ---------------------------------------------------------------------------
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Line 4\n")


# ---------------------------------------------------------------------------
# 6. FILE POINTER — seek(0) rewinds to the start of the file
# ---------------------------------------------------------------------------
# When you write() then immediately try to read() in the SAME open() call,
# the file pointer is sitting at the END. seek(0) moves it back to the start.
with open("my_file.txt", "w+", encoding="utf-8") as f:
    f.write("line content")
    f.seek(0)                       # rewind before reading, or read() returns ""
    content = f.read()
    print(content)


# ---------------------------------------------------------------------------
# 7. CSV FILES — csv module
# ---------------------------------------------------------------------------
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
]
with open("example.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)      # newline="" avoids extra blank rows on Windows

with open("example.csv", "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:           # each row comes back as a list of strings
        print(row)


# ---------------------------------------------------------------------------
# 8. EXCEL FILES — pandas (needs `pip install pandas openpyxl`)
# ---------------------------------------------------------------------------
# import pandas as pd
#
# data = {"Name": ["Ani", "Mikayel"], "Age": [25, 30], "City": ["Yerevan", "Gyumri"]}
# df = pd.DataFrame(data)
# df.to_excel("example.xlsx", index=False)       # write
#
# read_df = pd.read_excel("example.xlsx")         # read
# print(read_df)


# ---------------------------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------------------------
# with open(path, mode, encoding="utf-8") as f:   -> always use this pattern
# f.read()       -> whole file as one string
# f.readline()   -> one line at a time
# f.readlines()  -> list of all lines
# f.write(text)  -> write, no auto-newline
# f.seek(0)      -> rewind pointer to the start
