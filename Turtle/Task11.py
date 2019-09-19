from turtle import *
speed(0)
left(90)
for i in range(10):
    for k in range(90):
        forward(3 + i/2)
        left(4)
    for k in range(90):
        forward(3 + i/2)
        right(4)   
exitonclick()