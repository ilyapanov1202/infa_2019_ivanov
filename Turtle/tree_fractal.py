import turtle
from math import *
n = int(input())
l1 = 200
t3 = turtle
def tree(l, n, pos):
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.speed(1)
    t1.penup()
    t2.penup()
    t1.goto(pos)
    t2.goto(pos)
    t1.pendown()
    t2.pendown()
    angle = 180 / 3.1415926 * atan(pos[0]/(pos[1]+1))
    t1.left(angle)
    t2.left(angle)
    t1.left(30)
    t1.forward(l)
    t2.right(30)
    t2.forward(l)
    t1.ht()
    t2.ht()
    if n > 0:
        tree(l / 1.618, n - 1, t1.position())
        tree(l / 1.618, n - 1, t2.position())

tree(l1, n, t3.position())
t3.exitonclick()