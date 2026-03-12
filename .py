from turtle import *
t = Turtle()
t.hideturtle()

def right_rectangle():
    for i in range(3):
        t.forward(200)
        t.right(120)

t.color("black")
for i in range(3):
    t.begin_fill()
    right_rectangle()
    t.end_fill()
    t.left(120)

t.left(60)
t.color("yellow")
for i in range(3):
    t.begin_fill()
    right_rectangle()
    t.end_fill()
    t.left(120)
