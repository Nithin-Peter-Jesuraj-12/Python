from turtle import *
from random import *
pu(); ht(); bgcolor("black")
shape("square"); shapesize(2)
for i in range(5):
    for j in range(7):
        color(random(), random(), random())
        stamp(); fd(40)
    goto(0, ycor() + 40)
done()