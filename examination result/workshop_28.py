import os
import logging
import pandas as pd


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w+"
)

logging.info("Program started")

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logging.info(f"Directory created: {directory_name}")


def create_results_file(directory_name, file_name):
    create_directory(directory_name)
    file_path = os.path.join(directory_name, file_name)

    
    if not os.path.exists(file_path):
        data = {
            "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
            "Subject": ["Python", "Python", "Python", "Python", "Python"],
            "Score": [85, 92, 78, 88, 95]
        }
        df_initial = pd.DataFrame(data)
        df_initial.to_excel(file_path, index=False)
        logging.info(f"File created and saved: {file_path}")

    df = pd.read_excel(file_path)

  
    names = df["Name"]
    scores = df["Score"]

    number_of_students = len(df)
    highest_score = scores.max()
    lowest_score = scores.min()

    best_student = names[scores.idxmax()]
    worst_student = names[scores.idxmin()]

    
    print(f"Number of examined students: {number_of_students}")
    print(f"Best result: {best_student} - {highest_score}")
    print(f"Lowest result: {worst_student} - {lowest_score}")

    
    logging.info(f"Number of examined students: {number_of_students}")
    logging.info(f"Best result: {best_student} - {highest_score}")
    logging.info(f"Lowest result: {worst_student} - {lowest_score}")

if __name__ == "__main__":
    create_results_file("ExaminationResults", "student_data.xlsx")

import os
import shutil

def delete_directory(directory_name):
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
        print(f"Directory '{directory_name}' and all its contents are deleted.")
        
        # logging.info(f"Directory deleted: {directory_name}")
    else:
        print(f"Directory '{directory_name}' does not exist.")


# delete_directory("ExaminationResults")

