print()
name = input("What is your name? ")
print()
age = int(input("How old are you? "))
age_decade = age // 10
age_years = age % 10
print()
print(f"Your name is {name} and you are {age}.\n")
print(f"You are {age_decade} decades and {age_years} year(s) old.\n")