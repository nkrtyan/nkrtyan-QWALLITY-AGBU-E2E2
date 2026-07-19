from person.data import person
def get_full_name(name,surname):
    return f"{name} {surname}"

def print_person():
    name=person["name"]
    surname=person["surname"]
    full_name = get_full_name(name, surname)
    print(full_name)