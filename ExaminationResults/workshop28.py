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
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
        # TODO, need to add filemode
    )


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logging.info(f"Directory created: {directory_name}")
    # TODO, add also else branch

def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    pd.DataFrame(data).to_excel(file_path, index=False)
    logging.info(f"Excel file created: {file_path}")


def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.read_excel(file_path)

    names = df["Name"].tolist()
    scores = df["Score"].tolist()

    highest = max(scores)
    lowest = min(scores)

    best = [names[i] for i in range(len(scores)) if scores[i] == highest]
    worst = [names[i] for i in range(len(scores)) if scores[i] == lowest]

    logging.info(f"Number of examined students: {len(names)}")

    for student in best:
        logging.info(f"Best result: {student} - {highest}")

    for student in worst:
        logging.info(f"Lowest result: {student} - {lowest}")


def cleanup(directory_name):
    answer = input("Remove directory? Y/N: ")

    if answer.upper() == "Y" and os.path.exists(directory_name):
        shutil.rmtree(directory_name)
        logging.info(f"Directory removed: {directory_name}")
    else:
        logging.info(f"Directory was not removed: {directory_name}")


if __name__ == "__main__":
    setup_logging()

    directory = "ExaminationResults"
    file = "exam_results.xlsx"

    create_directory(directory)
    create_results_file(directory, file)
    analyze_results(directory, file)
    cleanup(directory)
# Nel, good job, working code