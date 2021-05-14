import turtle
t = turtle.Turtle()
color = ['red', 'blue', 'yellow', 'orange', 'purple']

t.hideturtle()
t.speed(0)
count = 1
angle = 121
step = 300
i = count
while i < step:
    t.pencolor(color[i%5])
    t.forward(i)
    t.left(angle)
    i += count
while i>0:
    t.pencolor(color[i%5])
    t.forward(i)
    t.left(angle)
    i = i - count
turtle.done()