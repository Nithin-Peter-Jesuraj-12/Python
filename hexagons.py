from turtle import *
colors =['yellow', 'blue','purple','green','pink']
for x in range(360):
    pencolor(colors[x%5])
    pensize(5)
    forward(x)
    left(40)
done()