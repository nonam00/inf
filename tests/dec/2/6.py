from turtle import *

tracer(0)
screensize(10000, 10000)
m = 20

for i in range(2):
    forward(13 * m)
    right(90)
    forward(20 * m)
    right(90)
up()
forward(8 * m)
right(90)
back(3 * m)
left(90)
down()
for i in range(2):
    forward(16 * m)
    right(90)
    forward(8 * m)
    right(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'red')

input()