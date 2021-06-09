import turtle as T
s=T.Screen()
s.bgcolor=("light green")
#T=turtle()
T.color("red")
T.shape("turtle")
T.up()
for s in range(5,10,20):
    T.stamp()
    T.forward(s)
    T.right(24)
T.done()