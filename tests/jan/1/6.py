from turtle import *

tracer(0)
screensize(1000, 1000)
m = 45
for i in range(6):
    for i in range(3):
        fd(7 * m)
        rt(120)
    rt(60)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
input()