from turtle import *

tracer(0)
screensize(10000, 10000)
m = 20

for i in range(2):
    forward(8 * m)
    right(90)
    forward(18 * m)
    right(90)

up()
forward(4 * m)
right(90)
forward(10 * m)
right(90)
down()

for i in range(2):
    forward(17 * m)
    right(90)
    forward(7 * m)
    right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
input()
