from turtle import *

screensize(1000, 1000)
tracer(0)
m = 20
for i in range(4):
    forward(3 * m)
    left(270)
    forward(5 * m)
    right(90)
left(270)
for i in range(3):
    forward(5 * m)
    right(90)
    forward(3 * m)
    left(270)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, "red")
input()
