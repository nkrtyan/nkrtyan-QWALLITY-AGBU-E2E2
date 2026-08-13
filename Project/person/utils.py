from Project.person import data

#TODO, keep two empty lines between functions
def get_full_name(name, surname):
    return name, surname


def print_person():
    person_data = data.my_dict
    name, surname = get_full_name(person_data['name'], person_data['surname'])
    print(f"{name} {surname}")
