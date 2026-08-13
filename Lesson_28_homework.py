import os
import logging
import pandas as pd

# Global data dictionary
data = {
    "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Score": [85, 92, 78, 88, 95]
}

# 1. Configure Logging
def setup_logging():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

# 2. Create Directory
def create_directory(directory_name="ExaminationResults"):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logging.info(f"Directory '{directory_name}' was created.")
    else:
        logging.info(f"Directory '{directory_name}' already exists.")

# 3. Create Excel File
def create_excel_file(directory_name="ExaminationResults", file_name="exam_results.xlsx"):
    file_path = os.path.join(directory_name, file_name)
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    logging.info(f"Excel file '{file_name}' was created at '{file_path}'.")
    return file_path

# 4. Analyze Exam Results
def analyze_results(file_path):
    df = pd.read_excel(file_path)
    

    results_df = df[["Name", "Score"]]

    total_students = len(results_df)
    
    max_idx = results_df["Score"].idxmax()
    best_student = results_df.loc[max_idx, "Name"]
    best_score = results_df.loc[max_idx, "Score"]
    
    min_idx = results_df["Score"].idxmin()
    lowest_student = results_df.loc[min_idx, "Name"]
    lowest_score = results_df.loc[min_idx, "Score"]
    
    # Logging key outcomes
    logging.info(f"Number of examined students: {total_students}")
    logging.info(f"Best result: {best_student} - {best_score}")
    logging.info(f"Lowest result: {lowest_student} - {lowest_score}")

if __name__ == "__main__":
    dir_name = "ExaminationResults"
    file_name = "exam_results.xlsx"
    
    setup_logging()
    create_directory(dir_name)
    file_path = create_excel_file(dir_name, file_name)
    analyze_results(file_path)