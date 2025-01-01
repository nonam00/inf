from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20
right(315)
for i in range(7):
    forward(n * 12)
    right(45)
    forward(6 * n)
    right(135)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()