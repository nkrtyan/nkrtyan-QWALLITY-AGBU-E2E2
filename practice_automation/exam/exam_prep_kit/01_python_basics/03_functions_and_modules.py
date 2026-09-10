"""
FUNCTIONS & MODULES CHEAT SHEET
================================
A function is a reusable block of code that runs only when called.
It takes input (arguments), does something, and (optionally) returns output.
"""

# ---------------------------------------------------------------------------
# 1. DEFINING & CALLING A FUNCTION
# ---------------------------------------------------------------------------
def greet(name):
    print(f"Hello, {name}!")

greet("Ani")   # calling the function — nothing happens until you call it


# ---------------------------------------------------------------------------
# 2. RETURN STATEMENT — sends a value back to the caller
# ---------------------------------------------------------------------------
def add(a, b):
    return a + b

result = add(2, 3)   # result = 5
# A function without an explicit `return` returns None.


# ---------------------------------------------------------------------------
# 3. TYPES OF ARGUMENTS — a favorite exam topic
# ---------------------------------------------------------------------------

# a) Required (positional) arguments — must be passed, in order
def describe_pet(animal, name):
    print(f"{name} is a {animal}")
describe_pet("dog", "Rex")

# b) Keyword arguments — pass by name, order doesn't matter
describe_pet(name="Rex", animal="dog")

# c) Default arguments — used when the caller doesn't supply a value
def describe_pet_default(animal, name="Buddy"):
    print(f"{name} is a {animal}")
describe_pet_default("cat")               # uses default name "Buddy"
describe_pet_default("cat", "Whiskers")   # overrides the default

# d) Variable-length arguments
#    *args  -> collects extra POSITIONAL args into a tuple
#    **kwargs -> collects extra KEYWORD args into a dict
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))   # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Ani", age=25, city="Yerevan")

# Order when combining them: (positional, *args, default, **kwargs)
def full_example(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)
full_example(1, 2, 3, 4, c=99, extra="hi")


# ---------------------------------------------------------------------------
# 4. LOCAL vs GLOBAL SCOPE
# ---------------------------------------------------------------------------
message = "I am global"   # defined at module (top) level -> global scope

def show_message():
    # This works: reading a global variable from inside a function is fine
    print(message)

def local_scope_example():
    local_var = "I only exist inside this function"
    print(local_var)
# print(local_var)  # <-- NameError here: local_var doesn't exist outside the function

def change_global_wrong():
    message = "trying to change it"   # this creates a NEW local variable, doesn't touch the global!

def change_global_right():
    global message                    # `global` keyword: explicitly modify the global variable
    message = "changed for real"


# ---------------------------------------------------------------------------
# 5. input() — getting data from the user (always returns a string!)
# ---------------------------------------------------------------------------
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))   # cast to int, since input() is always str


# ---------------------------------------------------------------------------
# 6. MODULES & IMPORTS
# ---------------------------------------------------------------------------
# A module is just a .py file. A package is a folder of modules containing __init__.py.
#
# import forms you must recognize:
#   import module_name
#   from module_name import name
#   from module_name import name as alt_name
#   import module_name as alt_name
#
# Examples (uncomment to try):
# import math
# print(math.sqrt(16))
#
# from math import sqrt, pi
# print(sqrt(16), pi)
#
# import math as m
# print(m.sqrt(16))

# Common built-in functions (always available, no import needed):
print(len([1, 2, 3]))   # length of an object
print(max(4, 9, 2))     # largest value
print(min(4, 9, 2))     # smallest value
print(sum([1, 2, 3]))   # sum of an iterable
print(round(3.14159, 2))  # rounds to 2 decimal places


# ---------------------------------------------------------------------------
# 7. if __name__ == "__main__":  — the "is this file being run directly?" guard
# ---------------------------------------------------------------------------
# When you RUN a script directly, Python sets its __name__ to "__main__".
# When you IMPORT that same script from another file, __name__ is set to the
# module's filename instead. This lets you write code that only runs when the
# file is executed directly (not when it's imported as a helper module).

def hello():
    print("Hello, World!")

if __name__ == "__main__":
    print("This script is being run directly.")
    hello()
