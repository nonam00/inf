from turtle import *
tracer(0)
screensize(10000, 10000)
n = 20
for i in range(3):
    left(90)
    for j in range(4):
        forward(5 * n)
        right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()