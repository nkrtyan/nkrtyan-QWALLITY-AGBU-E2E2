import os
import pandas
import logging
import shutil

data = {
    "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Score": [85, 92, 78, 88, 95]
}


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="app.log",
        filemode="a"
    )



def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"Directory is created: {directory_name}")

def create_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pandas.DataFrame(data)
    df.to_excel(file_path, index=False)
    logging.info(f"Excel{file_path} file is created")


def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pandas.read_excel(file_path)
    df = df[["Name", "Score"]]
    names = df["Name"]
    scores = df["Score"]
    total_students = len(df)
    highest_score = scores.max()
    lowest_score = scores.min()
    best_student = ""
    for i in range(len(df)):
        if df["Score"].iloc[i] == highest_score:
            best_student = df["Name"].iloc[i]
    lowest_student = ""
    for i in range(len(df)):
        if df["Score"].iloc[i] == lowest_score:
            lowest_student = df["Name"].iloc[i]
l.i

def cleanup(directory_name):
    answer = input("Do you want to remove the directory? (yes/no): ")
    if answer.lower() == "yes":
            if os.path.exists(directory_name):
                shutil.rmtree(directory_name)
                logging.info(f"Directory removed: {directory_name}")
    else:
        logging.info("Directory was not removed")

if __name__ == "__main__":
    setup_logging()
    create_directory("ExaminationResults")
    create_file("ExaminationResults", "exam_results.xlsx")
    analyze_results("ExaminationResults", "exam_results.xlsx")
    cleanup("ExaminationResults")