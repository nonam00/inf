from turtle import *
screensize(10000, 10000)
tracer(0)
n = 20

for i in range(100):
    forward(10 * n)
    right(180)
    forward(10 * n)
    right(198)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3, 'red')
input()