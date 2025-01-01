from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20
right(270)
for i in range(8):
    forward(10 * n)
    right(45)
    forward(10 * n)
    right(135)
for i in range(4):
    forward(4 * n)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()