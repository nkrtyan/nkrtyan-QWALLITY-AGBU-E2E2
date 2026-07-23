from Person.data import my_dic


def get_full_name(name, surname):
    return f"{name} {surname}"


def print_person():
    full_name = get_full_name(my_dic["name"], my_dic["surname"])
    print(full_name)