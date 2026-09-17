import os
import shutil
import logging
import pandas as pd

# TODO,  keep dict format
data = {
"Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
"Subject": ["Python", "Python", "Python", "Python", "Python"],
"Score": [85, 92, 78, 88, 95]
}

def setup_logging():
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w+'

    )

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logging.info(f"Directory '{directory_name}' was created.")
    else:
        logging.info(f"Directory '{directory_name}' already exists.")

   
def create_results_file(directory_name, file_name):

    file_path = os.path.join(directory_name, file_name)
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    logging.info(f"Results file '{file_name}' was created in directory '{directory_name}'.")

# TODO, keep two lines between functions
def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.read_excel(file_path)

    total_students = len(df)

    max_score = df['Score'].max()
    min_score = df['Score'].min()

    best_student = df[df['Score'] == max_score]['Name'].iloc[0]
    worst_student = df[df['Score'] == min_score]['Name'].iloc[0]

    logging.info(f'Number of examined students: {total_students}')
    logging.info(f'Best result: {best_student} - {max_score}')
    logging.info(f'lowest result: {worst_student} -{min_score}')

def cleanup(directory_name):
    user_input = input("Do you want to delete the directory and its contents? (yes/no): ")
    if user_input.lower() == 'yes':
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            logging.info(f"Directory '{directory_name}' was removed.")
        else:
            logging.info(f"Directory '{directory_name}' does not exist.")
    else:
        logging.info("Directory removal skipped by user.")

if __name__ == "__main__":
    setup_logging()
    logging.info('Starting the program')
    directory_name = "ExaminationResults"
    file_name = "exam_results.xlsx"

    create_directory(directory_name)
    create_results_file(directory_name, file_name)
    analyze_results(directory_name, file_name)
    cleanup(directory_name)
# Nel,  correct code