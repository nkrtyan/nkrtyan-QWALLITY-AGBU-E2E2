"""
import os
import shutil
import logging
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
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"Directory created: {directory_name}")
    else:
        logging.info(f"Directory already exists: {directory_name}")


def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.DataFrame(data)
    df.to_excel(file_path, index = False)
    logging.info(f"Excel file created: {file_path}")


def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.read_excel(file_path)
    names = df["Name"]
    scores = df["Score"]

    number_of_students = len(names)

    highest_score = scores.max()
    for i in range(len(df)):
        if df["Score"].iloc[i] == highest_score:
            best_student = df["Name"].iloc[i]
            break

    lowest_score = scores.min()
    for i in range(len(df)):
        if df["Score"].iloc[i] == lowest_score:
            lowest_student = df["Name"].iloc[i]
            break

    logging.info(
        f"Number of examined students: {number_of_students}"
    )

    logging.info(
        f"Best result: {best_student} - {highest_score}"
    )

    logging.info(
        f"Lowest result: {lowest_student} - {lowest_score}"
    )

    print(f"Number of examined students: {number_of_students}")
    print(f"Best result: {best_student} - {highest_score}")
    print(f"Lowest result: {lowest_student} - {lowest_score}")


def cleanup(directory_name):
    answer = input(
        f"Do you want to remove the directory "
        f"'{directory_name}'? Y/N: "
    )

    if answer.upper() == "Y":

        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)

            logging.info(
                f"Directory removed: {directory_name}"
            )

            print(
                f"Directory '{directory_name}' was removed."
            )

        else:
            logging.info(
                f"Directory not found: {directory_name}"
            )

            print("Directory does not exist.")

    else:
        logging.info(
            f"Directory was not removed: {directory_name}"
        )

        print("Directory was not removed.")


if __name__ == "__main__":

    directory_name = "ExaminationResults"
    file_name = "exam_results.xlsx"

    setup_logging()

    create_directory(directory_name)

    create_results_file(
        directory_name,
        file_name
    )

    analyze_results(
        directory_name,
        file_name
    )

    cleanup(directory_name)

"""


import os
import shutil
import logging
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
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name, exist_ok=True)
        logging.info(f"The folder '{directory_name}' has been created.")
    else:
        logging.info(f"Target folder '{directory_name}' already exists.")


def create_results_file(directory_name, file_name):
    destination_path = os.path.join(directory_name, file_name)
    results_frame = pd.DataFrame(data)
    results_frame.to_excel(destination_path, index=False)
    logging.info(f"Results successfully saved to {destination_path}")


def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.read_excel(file_path)
    names = df["Name"]
    scores = df["Score"]

    number_of_students = len(names)

    highest_score = scores.max()
    for i in range(len(df)):
        if df["Score"].iloc[i] == highest_score:
            best_student = df["Name"].iloc[i]
            break

    lowest_score = scores.min()
    for i in range(len(df)):
        if df["Score"].iloc[i] == lowest_score:
            lowest_student = df["Name"].iloc[i]
            break

    logging.info(
        f"Number of examined students: {number_of_students}"
    )

    logging.info(
        f"Best result: {best_student} - {highest_score}"
    )

    logging.info(
        f"Lowest result: {lowest_student} - {lowest_score}"
    )

    print(f"Number of examined students: {number_of_students}")
    print(f"Best result: {best_student} - {highest_score}")
    print(f"Lowest result: {lowest_student} - {lowest_score}")

def cleanup(directory_name):
    user_choice = input(f"Do you want to delete the directory '{directory_name}'? (Y/N): ").strip()

    if user_choice.upper() == "Y":
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            logging.info(f"Successfully deleted directory: {directory_name}")
            print(f"Directory '{directory_name}' was removed.")
        else:
            logging.info(f"Directory {directory_name} was not found for deletion.")
            print("Directory does not exist.")
    else:
        logging.info(f"User decided to keep the directory: {directory_name}")
        print("Directory was not removed.")


if __name__ == "__main__":
    target_dir = "ExaminationResults"
    target_file = "exam_results.xlsx"

    setup_logging()
    create_directory(target_dir)
    create_results_file(target_dir, target_file)
    analyze_results(target_dir, target_file)
    cleanup(target_dir)