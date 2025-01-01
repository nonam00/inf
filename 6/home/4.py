from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20

for i in range(4):
    forward(3 * n)
    left(270)
    forward(5 * n)
    right(90)
left(270)
for i in range(3):
    forward(5 * n)
    right(90)
    forward(3 * n)
    left(270)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()