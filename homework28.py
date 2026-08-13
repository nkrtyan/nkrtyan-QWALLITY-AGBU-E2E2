import os
import shutil
import logging
import pandas

data = {
        "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
        "Subject": ["Python", "Python", "Python", "Python", "Python"],
        "Score": [85, 92, 78, 88, 95]
        }

directory_name="ExaminationResults"
file_name="exam_results.xlsx"

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
    setup_logging(),
    create_directory(directory_name),
    create_results_file(directory_name, file_name),
    analyze_results(directory_name, file_name),
    cleanup(directory_name)









