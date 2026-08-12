import os

def creating_folder(folder_name, file_name, text):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    os.chdir(folder_name)

    with open(os.path.abspath(file_name), "w") as file:
        file.write(text)
        os.remove(file_name)

    os.chdir("..")

    answer = input("Do you want to remove the folder? (Y/N): ")
    os.rmdir(folder_name)

# if __name__ == "__main__":
    folder_name = "New folder"
    file_name = "New_file.txt"
    text = "Workshop information"

    creating_folder(folder_name, file_name, text)




from pathlib import Path
folder = Path("test")
folder.mkdir()
folder.mkdir(exist_ok=True)
folder = Path("project/files/documents")
folder.mkdir(parents=True, exist_ok=True)


import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")


import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Low memory")
logging.error("File not found")


import os
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder_name = "test"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    logging.info(f"Folder '{folder_name}' created")
else:
    logging.info(f"Folder '{folder_name}' already exists")

print(os.listdir())


import pandas as pd
print(pd.__version__)




from turtle import *
import colorsys as cs

speed(0)
pensize(2)
bgcolor("black")

h = 0

for i in range(400):
    c = cs.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005

    forward(i)
    right(59)

done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(360):
    c = cs.hsv_to_rgb(h, 1, 1)
    color(c)

    circle(100)
    right(10)

    h += 1 / 360

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(300):
    color(cs.hsv_to_rgb(h, 1, 1))
    forward(i)
    right(59)
    h += 1 / 300

hideturtle()
done()


from turtle import *

speed(0)
bgcolor("black")
color("cyan")
pensize(2)

for i in range(36):
    circle(100)
    right(10)

hideturtle()
done()


from turtle import *

speed(0)
bgcolor("black")
color("lime")
pensize(2)

for i in range(200):
    forward(i)
    right(91)

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(100):
    color(cs.hsv_to_rgb(h, 1, 1))

    for j in range(4):
        forward(i * 2)
        right(90)

    right(10)
    h += 1 / 100

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(72):
    color(cs.hsv_to_rgb(h, 1, 1))

    for j in range(5):
        forward(150)
        right(144)

    right(5)
    h += 1 / 72

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(500):
    color(cs.hsv_to_rgb(h, 1, 1))

    forward(i / 3)
    right(137)

    h += 0.002

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(100):
    color(cs.hsv_to_rgb(h, 1, 1))

    circle(i)
    right(20)

    h += 0.01

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(120):
    color(cs.hsv_to_rgb(h, 1, 1))

    forward(200)
    backward(200)

    right(3)

    h += 1 / 120

hideturtle()
done()


from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
pensize(2)

h = 0

for i in range(360):
    color(cs.hsv_to_rgb(h, 1, 1))

    forward(200)
    backward(200)

    right(1)

    h += 1 / 360

hideturtle()
done()