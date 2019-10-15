from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

def new_ball(a, b, c):
    global x, y, r
    canv.delete(ALL)
    x = a + rnd(1, 7)
    y = b + rnd(1, 7)
    r = c
    canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    #root.after(1000, click('<Button-1>'))

'''
def click(event):
    global counter
    if (x - event.x) ** 2 + (y - event.y) ** 2 < r ** 2:
        print("+1 point")
        counter += 1
        new_ball()
    else:
        print("miss")
        canv.delete(ALL)
        

new_ball()'''
x, y = 100, 100
r = 30
def click(event):
    new_ball(x, y, r)
    root.after(100, new_ball(200, 200, 20))

canv.bind('<Button-1>', click)


mainloop()
#print(counter)