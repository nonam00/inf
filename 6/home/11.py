from turtle import *
tracer(0)
screensize(10000, 10000)
n = 20
for i in range(2):
    forward(13 * n)
    right(90)
    forward(20 * n)
    right(90)
up()
forward(8 * n)
right(90)
back(3 * n)
left(90)
down()
for i in range(2):
    forward(16 * n)
    right(90)
    forward(8 * n)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()