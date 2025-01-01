from turtle import *
screensize(10000, 10000)
tracer(0)
n = 40
for i in range(6):
    for i in range(3):
        forward(7 * n)
        right(120)
    right(60)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()