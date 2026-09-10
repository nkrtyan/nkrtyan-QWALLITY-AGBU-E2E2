"""
PYTHON COLLECTIONS CHEAT SHEET
==============================
The 4 built-in collection types: list, tuple, dict, set.

Quick decision guide:
  - Need order + duplicates + mutable?         -> list
  - Need order + duplicates + read-only/fast?  -> tuple
  - Need key -> value lookup?                   -> dict
  - Need unique items, don't care about order?  -> set

Run this file top to bottom (python 01_collections.py) to see everything
print. Use Ctrl+F on this file during the exam.
"""

# ---------------------------------------------------------------------------
# 1. LIST — ordered, changeable (mutable), allows duplicates
# ---------------------------------------------------------------------------
colors = ["red", "green", "blue", "yellow", "white", "black"]

# Indexing: position starts at 0. Negative index counts from the end.
print(colors[0])    # 'red'   (first item)
print(colors[-1])   # 'black' (last item)
print(colors[4])    # 'white'
print(colors[-2])   # 'white' (second-to-last)

# Slicing: list[start:stop:step] -> stop is EXCLUSIVE
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[:5])     # [10, 20, 30, 40, 50]      first 5
print(nums[-3:])    # [70, 80, 90]              last 3
print(nums[:-2])    # [10..70]                  all but last 2
print(nums[::2])    # [10, 30, 50, 70, 90]      every 2nd item
print(nums[1::2])   # [20, 40, 60, 80]          every 2nd, starting at index 1
print(nums[::-1])   # reversed list

# Adding items
colors.append("purple")          # add single item to the end
colors.insert(2, "orange")       # insert "orange" at index 2 (shifts others right)
colors.extend(["gray", "pink"])  # append multiple items from another iterable

# Removing items
colors.remove("purple")          # removes the FIRST matching value (error if not found)
popped = colors.pop()            # removes & returns the LAST item (or pop(i) for index i)
popped_first = colors.pop(0)     # removes & returns item at index 0
del colors[0]                    # delete by index, no return value
# colors.clear()                 # would empty the whole list

# Checking membership — very common in exam questions
if "green" in colors:
    print("green is in the list")
if "purple" not in colors:
    print("purple is NOT in the list")

# Updating an item by index
colors[0] = "crimson"

# Useful built-ins / methods
print(len(colors))          # number of items
print(colors.index("blue")) # first index of a value (raises ValueError if missing)
print(colors.count("blue")) # how many times a value appears
nums_copy = nums.copy()     # shallow copy (don't just do nums_copy = nums — that's a reference!)
nums.sort()                 # sorts in place, ascending
nums.sort(reverse=True)     # sorts in place, descending
sorted_new = sorted(nums)   # returns a NEW sorted list, original untouched

# List comprehension — very exam-friendly, compact way to build a list
squares = [n**2 for n in range(5)]                 # [0, 1, 4, 9, 16]
evens_only = [n for n in nums if n % 2 == 0]        # filter with a condition
excluding_30 = [n for n in nums if n != 30]         # exclude one value


# ---------------------------------------------------------------------------
# 2. TUPLE — ordered, UNCHANGEABLE (immutable), allows duplicates
# ---------------------------------------------------------------------------
# Use () instead of []. Once created, you cannot add/remove/change items.
point = (10, 20)
rgb = ("red", "green", "blue")

print(rgb[0])       # indexing works just like a list: 'red'
print(rgb[1:])      # slicing works too: ('green', 'blue')

# rgb[0] = "black"  # <-- TypeError: 'tuple' object does not support item assignment

# "Updating" a tuple really means creating a brand-new tuple
rgb = rgb + ("purple",)     # note the trailing comma for a 1-item tuple!

# Tuple comparison is element-by-element, left to right (common exam gotcha)
a = (5, 6)
b = (5, 4)
print(a > b)   # True -> 5==5 (tie), then 6 > 4 decides it

# When to use tuple vs list:
#   tuple: fixed data, faster iteration, uses less memory, "read-only" intent
#   list:  data that will grow/shrink/change


# ---------------------------------------------------------------------------
# 3. DICTIONARY — key:value pairs, ordered (Python 3.7+), no duplicate keys
# ---------------------------------------------------------------------------
student = {"firstname": "Mike", "lastname": "Olsen", "year": 2019}

print(student["firstname"])          # direct access -> KeyError if key missing
print(student.get("age"))            # safe access -> returns None if missing
print(student.get("age", "N/A"))     # safe access with a default value

student["age"] = 21                  # add a new key
student["age"] = 22                  # update an existing key (same syntax!)
del student["age"]                   # remove a key
removed_value = student.pop("year")  # remove a key AND get its value back

# Iterating a dictionary — 3 common patterns, know all three
for key in student:                       # iterates over KEYS only
    print(key)
for key, value in student.items():        # iterates over key-value pairs (most useful)
    print(f"{key} -> {value}")
for value in student.values():            # iterates over VALUES only
    print(value)

print("firstname" in student)   # membership check applies to KEYS
print(len(student))             # number of key-value pairs

# Dict comprehension
squared_dict = {n: n**2 for n in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}


# ---------------------------------------------------------------------------
# 4. SET — unordered, unindexed, NO duplicate members
# ---------------------------------------------------------------------------
languages = {"python", "java", "python", "c++"}   # duplicate "python" is auto-removed
print(languages)             # {'python', 'java', 'c++'} (order not guaranteed)

languages.add("go")          # add a single item
languages.update(["rust", "kotlin"])  # add multiple items
languages.discard("java")    # remove if present, no error if missing
# languages.remove("java")   # remove — raises KeyError if missing

set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)   # union: {1, 2, 3, 4}
print(set_a & set_b)   # intersection: {2, 3}
print(set_a - set_b)   # difference: {1}
print(set_a ^ set_b)   # symmetric difference: {1, 4}

# You cannot index a set: languages[0] would raise TypeError
# Sets are great for de-duplicating a list quickly:
raw_list = [1, 2, 2, 3, 3, 3]
unique_items = list(set(raw_list))   # [1, 2, 3] (order not guaranteed)


# ---------------------------------------------------------------------------
# QUICK COMPARISON TABLE (for fast recall during the exam)
# ---------------------------------------------------------------------------
# Type   | Ordered | Mutable | Duplicates | Syntax
# -------|---------|---------|------------|----------
# list   |   Yes   |   Yes   |    Yes     |  [1, 2]
# tuple  |   Yes   |   No    |    Yes     |  (1, 2)
# dict   |   Yes*  |   Yes   | No dup keys|  {"a": 1}
# set    |   No    |   Yes   |    No      |  {1, 2}
# * dict preserves insertion order since Python 3.7, but you still access by key, not position.
