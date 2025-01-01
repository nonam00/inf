from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20
for i in range(13):
    forward(10 * n)
    right(90)
    forward(10 * n)
    right(90)
    forward(30 * n)
    right(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * n, y * n)
        dot(3, 'red')
input()