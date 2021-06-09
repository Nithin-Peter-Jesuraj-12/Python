import turtle as t
t.pensize(20)
t.bgcolor('skyblue')
t.speed(0)
for i in range(6):
    for colours in ['red','green','brown','orange','blue','white','black','yellow']:
        t.color(colours)
        t.circle(50)
        t.right(10)
t.done()
t.hideturtle()