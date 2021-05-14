import turtle

e = turtle.Turtle()

e.penup()
for i in range(30):
    e.stamp()
    e.left(i)
    e.forward(20)
e.home()
e.left(180)
for i in range(30):
    e.stamp()
    e.right(i)
    e.forward(20)
e.home()
e.left(180)
for i in range(30):
    e.stamp()
    e.left(i)
    e.forward(20)
e.home()
e.left(360)
for i in range(30):
    e.stamp()
    e.right(i)
    e.forward(20)


turtle.done()