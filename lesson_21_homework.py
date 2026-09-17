
'''This program code asks the users their age and converts it into decades and remaining years, then prints it.'''
age = int(input("How old are you? "))
decades = age // 10
years = age % 10
print(f"You are {decades} decades and {years} year(s) old.")