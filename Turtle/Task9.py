from turtle import *
shape('turtle')
for i in range(10):
    penup()
    goto(0, -(i+1)*(i+1) - 15)
    left(180/(i+3))
    pendown()
    for k in range(i+3):
        
        forward(50 + 5*i)
        left(360/(i+3))
    right(180/(i+3))
exitonclick()