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