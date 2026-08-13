import os

def creating_folder(folder_name, file_name, text):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    os.chdir(folder_name)
    with open(os.path.abspath(file_name), "w") as file:
        file.write(text)
    os.remove(file_name)    
    os.chdir("..")
    answer=input("Do you want remove the folder Y/N")
    if answer=="Y":
         os.rmdir(folder_name)


    
if __name__=="__main__":
    folder_name="New_folder"
    file_name="New_file"
    text="Workshop information"
    creating_folder(folder_name, file_name, text)

    print(os.getcwd())
    print(os.path.abspath(__file__))
    if os.path.isdir("directory"):
        print("It is a directory")
