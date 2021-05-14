import turtle
color = ['red', 'blue', 'yellow', 'green', 'purple']

t = turtle.Turtle()
for i in range(500):
    t.pencolor(color[i%5])
    t.forward(i)
    t.left(90)
turtle.done()