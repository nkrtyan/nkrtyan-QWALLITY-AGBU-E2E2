class MyClass:
    def __init__(self):
        self._protected_var = 42  # Protected variable

    def _protected_method(self):
        return "This is a protected method"

obj = MyClass()
# You can access protected members, but it's a convention to treat them as non-public.
print(obj._protected_var)       # Accessing a protected variable (not recommended)
print(obj._protected_method())  # Accessing a protected method (not recommended)
