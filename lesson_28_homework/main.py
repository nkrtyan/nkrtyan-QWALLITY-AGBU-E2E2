import logging
import os
import shutil
import pandas as pd


data = {
    "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Score": [85, 92, 78, 88, 95]
    }


def setup_logging():
    logging.basicConfig(
    level=logging.INFO,   
    format='%(asctime)s [%(levelname)s] %(message)s',   
    filename= "app.log",
    filemode='w+',
)


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logging.info(f"Directory {directory_name} was created.")
    else:
        logging.info(f"Directory {directory_name} already exists.")
 

def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    logging.info(f"Excel file {file_path} was created.")


def analyze_results(directory_name,file_name):
    file_path = os.path.join(directory_name, file_name)

    read_df = pd.read_excel(file_path)

    names = read_df["Name"].tolist()
    scores = read_df["Score"].tolist()

    high_score = scores[0]
    low_score = scores[0]

    high_score_student = []
    low_score_student = []

    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            high_score_student = [names[i]]

        elif scores[i] == high_score:
           high_score_student.append(names[i])

        # TODO, you can optimize here, using min , max functions
        if scores[i] < low_score:
            low_score = scores[i]
            low_score_student = [names[i]]

        elif scores[i] == low_score:
            low_score_student.append(names[i])


    number_of_students = len(read_df)

    for student in high_score_student: 
        logging.info(f"Best student: {student} - {high_score} points") 

    for student in low_score_student: 
        logging.info(f"Worst student: {student} - {low_score} points")

    logging.info(f"Number of examined students: {number_of_students}")


def cleanup(directory_name):
    ask_to_user = input("Would you like to remove folder, put Y/N: ")
    if ask_to_user == "Y":
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)

        logging.info(f"Directory {directory_name} is removed")
    else:
        logging.info(f"Directory {directory_name} wasn't removed")


if __name__ == "__main__":
    # TODO, keep dir_name = "ExaminationResults" and pass to all functions
    setup_logging()
    create_directory("ExaminationResults")
    create_results_file("ExaminationResults", "exam_results.xlsx")
    analyze_results("ExaminationResults", "exam_results.xlsx")
    cleanup("ExaminationResults")
# Nel, good job, working code