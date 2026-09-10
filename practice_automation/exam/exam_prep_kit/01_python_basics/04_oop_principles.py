"""
OOP PRINCIPLES CHEAT SHEET
============================
The 4 pillars: Encapsulation, Abstraction, Inheritance, Polymorphism.
This matters for Selenium too — Page Object Model (a common test-automation
pattern) is built entirely on classes and inheritance.
"""

# ---------------------------------------------------------------------------
# 1. CLASSES & OBJECTS — the basics
# ---------------------------------------------------------------------------
class Person:
    def __init__(self, fname, lname):
        # __init__ is the CONSTRUCTOR: runs automatically when you create an object.
        # `self` refers to the specific object being created/used — always the
        # first parameter of an instance method.
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")   # creates an object ("instance") of the Person class
x.printname()                # -> John Doe


# ---------------------------------------------------------------------------
# 2. ENCAPSULATION — bundling data + methods, controlling access
# ---------------------------------------------------------------------------
# Python doesn't have true "private" like Java/C#. It uses NAMING CONVENTIONS:
#   name          -> public:    freely accessible from anywhere
#   _name         -> protected: "please treat as internal" (convention only, still accessible)
#   __name        -> private:   name-mangled to _ClassName__name (harder, not impossible, to access)
class BankAccount:
    def __init__(self, balance):
        self.public_owner_note = "public info"      # public
        self._protected_notes = "internal use"       # protected (convention)
        self.__balance = balance                      # private (name-mangled)

    def get_balance(self):   # a "getter" — controlled access to private data
        return self.__balance

account = BankAccount(100)
print(account.get_balance())          # 100 — access via a method, the Pythonic way
# print(account.__balance)            # <-- AttributeError, name got mangled
print(account._BankAccount__balance)  # 100 — technically possible, but don't do this


# ---------------------------------------------------------------------------
# 3. INHERITANCE — a class taking on attributes/methods of another
# ---------------------------------------------------------------------------
# Person = parent/base class. Student = child/derived class.
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)   # super() calls the PARENT's __init__
        self.graduationyear = year        # then add child-specific attributes

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

s = Student("Mike", "Olsen", 2019)
s.printname()   # inherited method from Person -> Mike Olsen
s.welcome()      # Student's own method

# Gotcha: if a child class defines its OWN __init__ without calling super()
# (or Person.__init__(self, ...)), it OVERRIDES the parent's __init__ entirely
# and none of the parent's setup code runs automatically.


# ---------------------------------------------------------------------------
# 4. ABSTRACTION — hiding implementation details behind a required interface
# ---------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Consulting(ABC):          # inherits from ABC (Abstract Base Class)
    @abstractmethod              # marks this method as REQUIRED for subclasses
    def action(self):
        pass    # no implementation here — subclasses must provide one

class EngineerA(Consulting):
    def action(self):
        return "move 10 cm"

class EngineerB(Consulting):
    def action(self):
        return "some other action"

# Consulting()          # <-- TypeError: can't instantiate an abstract class directly
e1 = EngineerA()
e2 = EngineerB()
print(e1.action())
print(e2.action())

# Why bother? It forces every subclass to implement a required method,
# and it hides the "how" from whoever is using the class — useful in large
# codebases and when third parties (e.g. plugins) provide implementations.


# ---------------------------------------------------------------------------
# 5. POLYMORPHISM — same method name, different behavior per class
# ---------------------------------------------------------------------------
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

for animal in [Cat(), Dog()]:
    print(animal.sound())   # same method call, different result depending on the object


# ---------------------------------------------------------------------------
# 6. MULTIPLE INHERITANCE — a class inheriting from more than one parent
# ---------------------------------------------------------------------------
import datetime
from datetime import date

class Clock:
    def __init__(self):
        self.clock = datetime.datetime.now().time()

class Calendar:
    def __init__(self):
        self.calendar = date.today().strftime('%d/%m/%y')

class DayHour(Clock, Calendar):
    def __init__(self):
        Clock.__init__(self)      # when using multiple inheritance, calling each
        Calendar.__init__(self)   # parent's __init__ explicitly is often clearer than super()

dh = DayHour()
print(dh.calendar, dh.clock)


# ---------------------------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------------------------
# self               -> refers to the current instance, always first param of a method
# __init__           -> constructor, runs on object creation
# super().__init__() -> calls the parent class's constructor
# @abstractmethod     -> forces subclasses to implement this method
# _var / __var        -> protected / private naming convention
