import random  #1

secret_number = random.randint(1, 10)

print("Welcome to my game!")
print("I chose a number from 1 to 10.")

guess = int(input("Guess the number: "))

if guess == secret_number:
    print("Congratulations! You won!")
else:
    print("Sorry! You lost.")
    print("The correct number was:", secret_number)





import turtle #2

screen = turtle.Screen()
screen.title("My First Game")

player = turtle.Turtle()
player.shape("square")

def move_right():
    player.forward(20)

screen.listen()
screen.onkey(move_right, "Right")

screen.mainloop()




import tkinter as tk #3
import random

score = 0


def click_button():
    global score

    score += 1

    button.config(
        text=f"Score: {score}",
        command=click_button
    )

    x = random.randint(50, 350)
    y = random.randint(50, 250)

    button.place(x=x, y=y)


window = tk.Tk()

window.title("My First Game")
window.geometry("400x300")

button = tk.Button(
    window,
    text="Click me!",
    font=("Arial", 16)
)

button.place(x=150, y=120)

button.config(command=click_button)

window.mainloop()