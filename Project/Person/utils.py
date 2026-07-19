from .data import person
def get_full_name (name, surname):
    return  name + " " + surname
def print_person():
    full_name = get_full_name(person["name"], person["surname"])
    print(full_name)