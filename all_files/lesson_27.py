import os
import logging

def setup_logging():
    logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s [%(levelname)s] %(message)s', # Define the log message format
    datefmt='%m-%d-%Y',  # Define the date/time format
    filename='my_log1.log',  # Specify the log file
    filemode='a+',  # 'a' for appending, 'w' for overwriting the log file
	encoding='utf-8'  # Set the encoding to UTF-8
)

def creating_folder(folder_name, file_name, text):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    os.chdir(folder_name)
    logging.info(f"Directory '{folder_name}' created.")
    with open(os.path.abspath(file_name), "w") as file:
        file.write(text)
        logging.info(f"Text added to file '{file_name}'.")
    # os.remove(file_name)    
    # logging.info(f"File '{file_name}' removed.")
    os.chdir("..")
    answer=input("Do you want remove the folder Y/N")
    if answer=="Y":
         os.rmdir(folder_name)
    logging.info(f"Directory '{folder_name}' removed.")


    
if __name__=="__main__":
    setup_logging()
    folder_name="New_folder"
    file_name="New_file"
    text="Workshop information"
    creating_folder(folder_name, file_name, text)


    print(os.getcwd())
    print(os.path.abspath(__file__))
    if os.path.isdir("directory"):
        print("It is a directory")
