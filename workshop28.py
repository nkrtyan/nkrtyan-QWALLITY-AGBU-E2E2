import os
import pandas as pd
import shutil
import logging

data = {
    "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Score": [85, 92, 78, 88, 95],
}

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="app.log",
        format="%(asctime)s - %(levelname)s - %(message)s"
        #  TODO, add filemode
    )

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"Directory '{directory_name}' created.")
    else:
        logging.info(f"Directory '{directory_name}' already exists.")

# TODO, keep two lines between functions
def create_results_file(directory_name, file_name):
    df= pd.DataFrame(data)
    file_path = os.path.join(directory_name, file_name)
    df.to_excel(file_path, index=False)
    logging.info(f"Results data saved to '{file_path}'.")

def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.read_excel(file_path)
    names = df["Name"]
    scores = df["Score"]
    num_students = len(names)
    highest_score = scores.max() # TODO,  not used
    lowest_score = scores.min() # TODO,  not used
    logging.info(f"Number of examined students: {num_students}")
    # TODO,  you should log also best student name, and low student name
    
# analyze results function is not finished yet
def cleanup(directory_name):
    answer = input(f"Do you want to remove the directory '{directory_name}'? (y/n): ").strip().lower()
    if answer == "y":
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            logging.info(f"Directory '{directory_name}' removed.")
        else:
            logging.info(f"Directory '{directory_name}' does not exist, nothing to remove.")
    else:
        logging.info(f"Directory '{directory_name}' was kept (user chose not to remove it).")

if __name__ == "__main__":
    directory_name = "ExaminationResults"
    file_name = "exam_results.xlsx"
 
    setup_logging()
    create_directory(directory_name)
    create_results_file(directory_name, file_name)
    analyze_results(directory_name, file_name)
    cleanup(directory_name)

# Nel, mainly code is correct, have a look to TODO