from turtle import *
for i in range(10):
    color('white')
    goto(-10*i, -10*i)
    color('black')
    for k in range(4):
        forward(20*(i+1))
        left(90)
    
exitonclick()