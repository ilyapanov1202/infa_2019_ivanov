from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
points_1 = 0

class ball():
    def __init__(self, x=40, y=450):
	self.x = x
	self.y = y
	self.r = 10
	self.vx = 0
	self.vy = 0
	self.color = choice(['blue', 'green', 'red', 'brown'])
	self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)
	self.line = 30
	
    def set_coords(self):
	canv.coords(self.id,self.x - self.r,self.y - self.r,self.x + self.r,self.y + self.r)
    
    def move(self):
	global balls
	if self.x < self.r and self.vx < 0:
	    self.vx *= -0.8
            
	if self.x > 800 - self.r and self.vx > 0:
	    self.vx *= -0.8
	
	if self.y < self.r and self.vy > 0:
	    self.vy *= -0.8
            
	if self.y > 600 - self.r and self.vy < 0:
	    self.vy *= -0.8
	    if self.vy < 5:
		self.vy *= 0.6
	    if self.vy < 0.5:
		self.vy = 0
	
	self.x += self.vx
	self.y -= self.vy
	self.vy -= 1
	self.vx *= 0.98
	self.vy *= 0.98
	if abs(self.vx) < 5:
	    self.vx *= 0.96
	
	self.set_coords()
	print(self.y, self.r, self.y + self.r)
	if 5 * abs(self.vx) + abs(self.vy) < 1 and self.y + self.r > 799:
	    canv.delete(self.id)
	    balls.remove(self)



    def hittest(self, obj):
        ans = False
        if (self.x-obj.x)**2 + (self.y-obj.y)**2 <= (obj.r + self.r)**2:
	    ans = True
        return ans


class gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


id_points = canv.create_text(30,30,text = points_1,font = '28')
class target():
    def __init__(self):
        global id_points
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()

    def new_target(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):

        global points_1
        points_1 += points
        canv.itemconfig(id_points, text=points_1)
        canv.delete(self.id)



screen1 = canv.create_text(400, 300, text='', font='28')

bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    g1 = gun()
    t1 = target()
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls :
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()

    canv.itemconfig(screen1, text='')
    canv.delete(g1.id)

    root.after(750, new_game)


new_game()

root.mainloop()
