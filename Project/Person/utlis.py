from Person.data import my_data

def get_full_name(name, surname):
    return name + " " + surname


def print_person():
    name = my_data["name"]
    surname = my_data["surname"]

    full_name = get_full_name(name, surname)
    print(full_name)
