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