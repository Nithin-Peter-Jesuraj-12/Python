import turtle as t
t.bgcolor('black')
t.pensize(2)
t.speed(20)
for i in range(6):
    for c in ['red','magenta','blue','cyan','green','yellow','white']:
        t.color(c)
        t.circle(150)
        t.circle(100)
        t.circle(50)
        t.left(10)
t.hideturtle()