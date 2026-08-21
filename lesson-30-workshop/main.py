from animal_classes import Cat
import logging

def setup_logging():
    logging.basicConfig(
    level=logging.INFO,   
    format='%(asctime)s [%(levelname)s] %(message)s',   
    filename= "info.log",
    filemode='w+',
)


if __name__ == "__main__":
    setup_logging()
    logging.info("Application started")

    name=input("Input cat name: ")
    age = int(input("Enter age: "))
    height = int(input("Enter height: "))

    cat = Cat(name, age, height)
    logging.info("Cat created")

    cat.showinfo()
    cat.move()
    category = cat.get_category()
    print(category)
    
    logging.info("Application finished")