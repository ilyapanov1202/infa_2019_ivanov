from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

l = Label(root, bg = "black", fg = "white", font = "Arial 36", width = 4)
l.pack()

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    #root.after(1000, new_ball)

flag = 0
def new_bomb():
    global x2, y2, r2, flag
    if flag == 1:
        canv.delete(bomb1, bomb2)
    x2 = rnd(100, 700)
    y2 = rnd(100, 500)
    r2 = rnd(50, 80)
    bomb1 = create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill = 'red', width = 0)
    bomb2 = create_oval(x2 - r2 + 10, y2 - r2 + 10, x2 + r2 - 10, y2 - r2 + 10, fill = 'white', width = 0)
    canv.bomb1
    flag = 1
    root.after(1000, new_bomb)
    

counter = 0
def click(event):
    global counter
    if (x - event.x) ** 2 + (y - event.y) ** 2 < r ** 2:
        print("+1 point")
        counter += 1
        new_ball()
        l['text'] = ' '.join(str(counter))
    else:
        print("miss")
        #canv.delete(ALL)
        

new_bomb()
new_ball()
canv.bind('<Button-1>', click)
mainloop()
print(counter)