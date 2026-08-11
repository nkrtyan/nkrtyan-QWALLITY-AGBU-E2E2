import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s [%(levelname)s] %(message)s', # Define the log message format
    datefmt='%m-%d-%Y',  # Define the date/time format
    filename='my_log.log',  # Specify the log file
    filemode='a+',  # 'a' for appending, 'w' for overwriting the log file
	encoding='utf-8'  # Set the encoding to UTF-8
)

if __name__ == "__main__":
    if 1==2:
        logging.info("This is an info message")
    else:
        logging.error("This is an error message")

        import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def manage_directory(dir_name, file_name, text):
    try:
        # Step 1: Check and create directory
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            logging.info(f"Directory '{dir_name}' created.")
        else:
            logging.info(f"Directory '{dir_name}' already exists.")

        # Step 2: Create file path
        file_path = os.path.join(dir_name, file_name)

        # Step 3: Create and append text to file
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(text + "\n")
            logging.info(f"Text added to file '{file_name}'.")

        # Step 4: Remove file
        os.remove(file_path)
        logging.info(f"File '{file_name}' removed.")

        # Step 5: Remove directory
        os.rmdir(dir_name)
        logging.info(f"Directory '{dir_name}' removed.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example call
manage_directory("test_dir", "example.txt", "Hello, logging!")