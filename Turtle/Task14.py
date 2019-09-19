import turtle
t1 = turtle
t2 = turtle
for k in range(5):
    t1.forward(100)
    t1.left(720/5)
t2.penup()
t2.goto(200, 0)
t2.pendown()
for k in range(11):
    t2.forward(100)
    t2.left(1800/11)
t1.exitonclick()