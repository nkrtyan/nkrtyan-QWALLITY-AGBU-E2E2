from all_files.Project.person import data

data.dict1

def  get_full_name(name, surname):
    return name + " " + surname


def print_person():
    print(data.dict1["name"], data.dict1["surname"])



