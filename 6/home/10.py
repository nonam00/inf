from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20
for i in range(10):
    for j in range(3):
        forward(10 * n)
        right(90)
        forward(10 * n)
        right(270)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()
#19 * 10 * 4 + 39 * 39