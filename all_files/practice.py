import os

folder_name="New_folder"
file_name="New_file"

def homework(folder_name, file_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    os.chdir(folder_name)
    with open(os.path.abspath(file_name), "w") as file:
        file.write("Workshop information")

    os.remove(file_name)
    os.chdir("..")
    answer=input("Do you want remove the folder Y/N")
    if answer=="Y":
        os.rmdir(folder_name)
    print(os.getcwd())

if __name__=="__main__":
    homework(folder_name, file_name)