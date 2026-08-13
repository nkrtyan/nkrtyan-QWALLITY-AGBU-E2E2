import os
import logging
import shutil
import pandas

data = {
    "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Score": [85, 92, 78, 88, 95]
}

directory_name="ExaminationResults"
file_name="exam_results.xlsx"

def setup_logging():
        logging.basicConfig (
        level=logging.INFO,  
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m-%d-%Y', 
        filename='app.log',  
        filemode='w+',  
        encoding='utf-8'  
)

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"Directory '{directory_name}' was created.")
    else:
        logging.info(f"Directory '{directory_name}' already exists.")


def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pandas.DataFrame(data)
    df.to_excel(file_path, index=False)
    logging.info(f"Excel file '{file_name}' was created.")

def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    df = pandas.read_excel(file_path)
    print(df)
    # logging.info(f"Number of examined students: {len(df['Name'])}")
    for i in range(len(df['Name'])):
        logging.info(f"Best result: {df['Name'][i]}, Score: {df['Score'][i]}")
    # logging.info(f"Best result: {df['Score'].max()}")
    logging.info(f"Lowest result: {df['Score'].min()}")
    # for i in range(len(df['Name'])):
    #     logging.info(f"Student: {df['Name'][i]}, Score: {df['Score'][i]}")

def cleanup(directory_name):
    if os.path.exists(directory_name):
        answer=input("Do you want to remove the folder? (Y/N): ")
        if answer.upper() == "Y":
            shutil.rmtree(directory_name)
    logging.info(f"Directory '{directory_name}' was deleted.")

if __name__ == "__main__":
    setup_logging()
    create_directory(directory_name)
    create_results_file(directory_name, file_name)
    analyze_results(directory_name, file_name)
    # cleanup(directory_name)