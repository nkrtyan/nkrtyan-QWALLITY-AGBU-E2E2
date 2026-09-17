"""
DECISION-MAKING STATEMENTS & LOOPS CHEAT SHEET
===============================================
if / elif / else, for, while, nested loops, break/continue/pass.

Reminder: Python has no curly braces {} — indentation (4 spaces, be consistent!)
defines a block. This is the #1 source of syntax errors for beginners.
"""

# ---------------------------------------------------------------------------
# 1. IF / ELIF / ELSE
# ---------------------------------------------------------------------------
total = 60
country = "US"

# if: runs only when condition is True
if total > 50:
    print("Order qualifies for a discount")

# if / else: exactly one of the two branches runs
if total > 100:
    print("Big order")
else:
    print("Regular order")

# if / elif / else: elif = "else if", checked in order, first True one wins
# (this exact shipping example is straight from the course slides)
if country == "US":
    if total <= 50:
        print("Shipping Cost is $50")
    elif total <= 100:
        print("Shipping Cost is $25")
    elif total <= 150:
        print("Shipping Cost is $5")
    else:
        print("FREE")
elif country == "AU":
    if total <= 50:
        print("Shipping Cost is $100")
    else:
        print("Other shipping cost")
else:
    print("Shipping not available")

# Comparison & logical operators you'll need:
#   ==  !=  >  <  >=  <=        and   or   not
# Membership / identity operators:
#   in   not in                 is   is not
number_list = [10, 23, 45, 67, 88, 92]
entered_number = 45
if entered_number in number_list:
    print(f"{entered_number} exists in the list")
    if entered_number % 2 == 0:
        print("...and it's even")
    else:
        print("...and it's odd")
else:
    print(f"{entered_number} is not in the list")


# ---------------------------------------------------------------------------
# 2. FOR LOOP — iterate over a known sequence (list, string, range, etc.)
# ---------------------------------------------------------------------------
for color in ["red", "green", "blue"]:
    print(color)

# range(start, stop, step) — stop is EXCLUSIVE, default start=0, default step=1
for i in range(5):            # 0,1,2,3,4
    print(i)
for i in range(2, 6):         # 2,3,4,5
    print(i)
for i in range(10, 0, -2):    # 10,8,6,4,2 (counting down)
    print(i)

# Looping with both index and value — enumerate() is the Pythonic way
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Looping over a slice of a list by index
number_list = [10, 23, 45, 67, 88, 92, 34, 56, 78]
for i in range(2, 6):
    print(f"At index {i}, the number is: {number_list[i]}")

# List comprehension is often a cleaner replacement for a simple for-loop
my_list = [1, 3, 5, 7, 9]
new_list = [n for n in my_list if n != 5]   # every item except 5


# ---------------------------------------------------------------------------
# 3. WHILE LOOP — repeats WHILE a condition stays True
# ---------------------------------------------------------------------------
count = 0
while count < 5:
    print(count)
    count += 1     # don't forget to update the condition variable, or infinite loop!

# while True + break is a common pattern for "loop until a condition is met"
attempts = 0
while True:
    attempts += 1
    if attempts >= 3:
        break
print(f"Stopped after {attempts} attempts")


# ---------------------------------------------------------------------------
# 4. NESTED LOOPS — a loop inside another loop
# ---------------------------------------------------------------------------
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()  # newline after each row


# ---------------------------------------------------------------------------
# 5. LOOP CONTROL STATEMENTS: break / continue / pass
# ---------------------------------------------------------------------------
# break: exits the loop entirely, right now
for n in range(10):
    if n == 5:
        break
    print(n)   # prints 0,1,2,3,4 then stops

# continue: skips the rest of THIS iteration, moves to the next one
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)   # prints only odd numbers: 1,3,5,7,9

# pass: does nothing — a placeholder so the code is syntactically valid
for n in range(5):
    if n == 3:
        pass   # TODO: handle this case later
    print(n)

# pass is also used for empty function/class bodies while you're stubbing things out:
def not_implemented_yet():
    pass
