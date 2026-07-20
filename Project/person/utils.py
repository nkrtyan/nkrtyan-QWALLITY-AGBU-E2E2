from person.data import person_data


def get_full_name(name, surname):
    return f"{name} {surname}"


def print_person():
    my_name = person_data["name"]
    my_surname = person_data["surname"]
    full_name = get_full_name(my_name, my_surname)
    print(f"Full Name: {full_name}")