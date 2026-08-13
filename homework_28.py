import os
import shutil
import logging
import pandas as pd

# Global Dictionary
data = {
    "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Score": [85, 92, 78, 88, 95]
}

#1.Logging
# Create a function to configure logging.

def setup_logging():
        logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='app.log',
        filemode='a'
    )

#2. Create Directory
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"Directory '{directory_name}' is created")
    else:
        logging.info(f"Directory '{directory_name}' already exists")
        print(f"Directory '{directory_name}' already exists")

#3. Create Excel File
def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

    logging.info(f"File '{file_path}' was created")
    
#4. Analyze Exam Results
def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pd.read_excel(file_path)
    names = df["Name"]
    scores = df["Score"]

    number_of_students = len(scores)
    highest_score = scores.max()
    lowest_score = scores.min()

   
    highest_index = scores.idxmax()
    lowest_index = scores.idxmin()

    best_student = names[highest_index]
    worst_student = names[lowest_index]

    logging.info(f"Number of examined students: {number_of_students}")
    logging.info(f"Best result: {best_student} - {highest_score}")
    logging.info(f"Lowest result: {worst_student} - {lowest_score}")

    
#5. Cleanup
def cleanup(directory_name):
    answer = input(f"Do you want to remove the directory '{directory_name}'? (yes/no)\n")
    if answer.lower() == "yes":
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            logging.info(f"Directory '{directory_name}' was removed")
        else:
            logging.info(f"Directory '{directory_name}' does not exist")
            print(f"Directory '{directory_name}' does not exist")
    else:
        logging.info("User chose not to remove the directory")
        

if __name__ == "__main__":
    directory_name = "ExaminationResults"
    file_name = "exam_results.xlsx"

    setup_logging()
    create_directory(directory_name)
    create_results_file(directory_name, file_name)
    analyze_results(directory_name, file_name)
    cleanup(directory_name)

# Nel, very accurate working code, good for you