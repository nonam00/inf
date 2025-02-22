from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20
for i in range(2):
    forward(8 * n)
    right(90)
    forward(18 * n)
    right(90)
up()
forward(4 * n)
right(90)
forward(10 * n)
right(90)
down()
for i in range(2):
    forward(17 * n)
    right(90)
    forward(7 * n)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()