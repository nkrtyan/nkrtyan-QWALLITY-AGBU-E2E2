import os
import shutil
import logging
import pandas

data = {
        "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
        "Subject": ["Python", "Python", "Python", "Python", "Python"],
        "Score": [85, 92, 78, 88, 95]
        }



def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m-%d-%Y', 
        filename='app.log', 
        filemode='w',  
	    encoding='utf-8'  
)
pass


def create_directory(directory_name):
    if os.path.exists(directory_name):
        logging.info(f"{directory_name} exists.")
    else:
        os.mkdir(directory_name)
        logging.info(f"{directory_name} was created" )
pass


def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pandas.DataFrame(data)
    df.to_excel(file_path, index=False)
    logging.info(f"The excel file {file_name} was created")
pass

def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    read_df = pandas.read_excel(file_path)
    print(read_df)
    name=read_df["Name"]
    score=read_df["Score"]
    logging.info(f"Number of examined students:{len(name)}")
    for item in range(len(name)):
        if score[item]==max(score):
            logging.info(f"Best result: {name[item]} - {max(score)}")
    for item in range(len(name)):
        if score[item]==min(score):
            logging.info(f"Lowest result: {name[item]} - {min(score)}") 

pass


def cleanup(directory_name):
    if os.path.exists(directory_name):
        answer=input(f"Do you want remove {directory_name} Y/N")
        if answer=="Y":
            shutil.rmtree(directory_name)
    logging.info(f"Directory {directory_name} and all its contents have been removed.")

pass


if __name__ == "__main__":
    directory_name="ExaminationResults"
    file_name="exam_results.xlsx"
    setup_logging(),
    create_directory(directory_name),
    create_results_file(directory_name, file_name),
    analyze_results(directory_name, file_name),
    cleanup(directory_name)



"""Task: University Examination Results
Story
A university needs a Python program to manage students' Python exam results.
The program should create a folder, save exam results to an Excel file, analyze the results,
log the main actions, and optionally remove the folder at the end.

Data
Use this global dictionary:
data = {
"Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
"Subject": ["Python", "Python", "Python", "Python", "Python"],
"Score": [85, 92, 78, 88, 95]
}

Requirements
1. Logging
Create a function to configure logging.
• Save logs to app.log
• Use INFO level
• Include date, log level, and message

2. Create Directory
Create a function that:
• Accepts the directory name as an argument (ExaminationResults)
• Function should create it does not exist
• Logs that the directory was created

3. Create Excel File
Create a function that:
• Accepts the directory name and file name as arguments
• Creates exam_results.xlsx inside
• Writes the global exam data to the Excel file
• Logs that the file was created

4. Analyze Exam Results
Create a function that:
• Reads the Excel file
• Takes the Name and Score columns
• Finds how many students took the exam
• Finds the highest score
• Finds the lowest score
• Finds the names of the students with the highest and lowest scores
• Logs results
Example logs:
INFO - Number of examined students: 5
INFO - Best result: Sophia - 95
INFO - Lowest result: Emma – 78

5. Cleanup
Create a function that:
• Asks the user if they want to remove the directory
• Checks if the directory exists
• Uses shutil.rmtree() to remove the directory and all files inside it
• Logs whether the directory was removed

Technical Requirements
Use separate functions:
def setup_logging():
pass

def create_directory(directory_name):
pass

def create_results_file(directory_name, file_name):
pass

def analyze_results(directory_name, file_name):
pass

def cleanup(directory_name):
pass

Use: if __name__ == "__main__":"""





