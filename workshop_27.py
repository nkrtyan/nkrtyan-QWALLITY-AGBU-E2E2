import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def create_and_write(dir_name, file_name, text):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        logging.info(f"Created directory: {dir_name}")
    else:
        logging.debug(f"Directory already exists: {dir_name}")

    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'a') as file:
        file.write(text + '\n')
    logging.info(f"Appended text to: {file_path}")

    return file_path


def cleanup(dir_name, file_name):
    file_path = os.path.join(dir_name, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        logging.info(f"Removed file: {file_path}")

    if os.path.exists(dir_name):
        os.rmdir(dir_name)
        logging.info(f"Removed directory: {dir_name}")


if __name__ == "__main__":
    dir_name = "my_dir"
    file_name = "my_file.txt"
    text = "This is a text for testing."

    create_and_write(dir_name, file_name, text)
    cleanup(dir_name, file_name)