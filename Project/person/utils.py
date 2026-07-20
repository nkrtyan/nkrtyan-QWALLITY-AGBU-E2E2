from person.data import person_data
def get_full_name(name, surname):
    return f"{name} {surname}"
def print_person():
    name = person_data["name"]
    surname = person_data["surname"]
    full_name = get_full_name(name,surname)
    print(full_name)