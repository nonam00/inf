from turtle import * 
screensize(1000, 1000)
tracer(0)
m = 10
right(270)
for i in range(8):
    forward(10 * m)
    right(45)
    forward(10 * m)
    right(135)
for i in range(4):
    forward(4 * m)
    right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, "red")
input()
