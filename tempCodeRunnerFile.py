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