from turtle import *
tracer(0)
screensize(1000, 1000)
m = 20
for i in range(3):
    left(90)
    for j in range(4):
        forward(5 * m)
        right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, "red")
input()
