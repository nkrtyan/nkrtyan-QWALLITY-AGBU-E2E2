from person.data import person_dict
def get_full_name(name, surname):
    return f"{name} {surname}"
def print_person():
    full_name = get_full_name(person_dict["name"], person_dict["surname"])
    print(full_name)