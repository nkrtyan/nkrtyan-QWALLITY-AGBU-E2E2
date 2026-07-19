"""Create a function get_full_name(name, surname) that takes two arguments and returns the person's full name. 
Create another function print_person() that retrieves the values from the dictionary and prints the full name. 
"""

from .data import person

def get_full_name(name, surname):
     return f"{name} {surname}"

def print_person():
    full_name = get_full_name(person["name"], person["surname"])
    print(full_name) 
