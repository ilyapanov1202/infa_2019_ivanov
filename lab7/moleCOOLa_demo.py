

from tkinter import *

from random import randrange as rnd

import time

root = Tk()

root.geometry('185x170')





entry_text1 = StringVar()
entry1 = Entry(root, textvariable = entry_text1, font = "Arial 36", bd = 12, width = 6)
entry1.insert(0, "")
entry1.place(relx = 0, rely = 0)

def entry1_get():
    global gravity, entry_text2, entry2, button2, root
    gravity = int(entry_text1.get()) * 2000
    button1.destroy()
    entry1.destroy()
    
    entry_text2 = IntVar()
    entry2 = Entry(root, textvariable = entry_text2, font = "Arial 36", bd = 12, width = 6)
    entry2.insert(0, "")
    entry2.place(relx = 0, rely = 0)
    
    button2 = Button(root, text = "Elasticity coefficient\n (from 1 to 100)", font = "Arial 14", command = entry2_get)
    button2.place(relx = 0, rely = 0.5)
    

def entry2_get():
    global elasticity_coefficient, entry_text2, entry2, button2, root, canv
    elasticity_coefficient = int(entry_text2.get()) * 100000
    main()
    button2.destroy()
    entry2.destroy()
    root.geometry('800x600')


button1 = Button(root, text = "Gravity", font = "Arial 32", width = 7, command = entry1_get)
button1.place(relx = 0, rely = 0.5)



class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self
    
    def __imul__(self, c):
        self.x *= c
        self.y *= c
        return self
    
    def __mul__(self, c):
        return Vector(self.x * c, self.y * c)
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def module(self, vector):
        return ((self.x - vector.x) ** 2 + (self.y - vector.y) ** 2) ** 0.5
    
    def show(self):
        print("(%s; %s)" % (self.x, self.y))



class Ball:
    def __init__(self, x, y, v_x, v_y, a_x, a_y, r, flag):
        self.position = Vector(x, y)
        self.speed = Vector(v_x, v_y)
        self.acceleration = Vector(a_x, a_y)
        self.radius = r
        self.flag = flag
        self.obj = canv.create_oval(x - r, y - r, x + r, y + r, fill = "#" + str(int(r ** 2 / 45)) + str(int(r ** 2 / 60)) + str(int(r ** 2 / 45)))
    
    def paint(self):
        self = Ball(self.position.x, self.position.y, self.speed.x, self.speed.y, self.acceleration.x, self.acceleration.y, self.radius, self.flag)
        
    #|||-----------------------------------------function is not used>>>
    def move(self, dt):
        canv.move(self.obj, self.speed.x * dt, self.speed.y * dt)
        self.calculate_speed(dt)
        self.calculate_position(dt)
        self.flag = 0
    #-----------------------------------------<<<function is not used|||
    
    def move_to(self, dt):
        self.calculate_speed(dt)
        self.calculate_position(dt)        
        self.paint()
        self.flag = 0
        
    def calculate_speed(self, dt):
        self.speed += self.acceleration * dt
        if abs(self.speed.x) > 5000:
            self.speed.x = abs(self.speed.x) % 5000 * (self.speed.x / abs(self.speed.x))
        if abs(self.speed.y) > 5000:
            self.speed.y = abs(self.speed.y) % 5000 * (self.speed.y / abs(self.speed.y))
        
    def calculate_position(self, dt):
        self.position += self.speed * dt
    
    def show(self):
        print("pos = (%s; %s)" % (self.position.x, self.position.y), "\nv = (%s; %s)" % (self.speed.x, self.speed.y), "\na = (%s; %s)" % (self.acceleration.x, self.acceleration.y), "\nr =", self.radius)
    
    def collision(self, ball):
        global elasticity_coefficient, gravity
        
        if self.position.module(ball.position) < self.radius + ball.radius:
            dx = self.radius + ball.radius - self.position.module(ball.position)
            self.acceleration = (self.position + ball.position * (-1)) * ((elasticity_coefficient * dx ** 2 / self.radius ** 2) / self.position.module(ball.position))
            ball.acceleration = (ball.position + self.position * (-1)) * ((elasticity_coefficient * dx ** 2 / ball.radius ** 2) / self.position.module(ball.position))
            self.flag = 1
            ball.flag = 1
            
        if self.flag == 0:
            self.acceleration = Vector(0, gravity)
        
    def wall_collision(self):
        if self.position.x < self.radius and self.speed.x < 0:
            self.speed.x *= -1
            if self.speed.x < 5:
                self.speed.x = 5
        if self.position.x > 800 - self.radius and self.speed.x > 0:
            self.speed.x *= -1
            if self.speed.x > -5:
                self.speed.x = -5
        if self.position.y < self.radius and self.speed.y < 0:
            self.speed.y *= -1
            if self.speed.y < 5:
                self.speed.y = 5
        if self.position.y > 600 - self.radius and self.speed.y > 0:
            self.speed.y *= -1
            if self.speed.y > -5:
                self.speed.y = -5
            self.acceleration.y = 0


class World:
    def __init__(self, dt):
        self.dt = dt
    
    def create_balls(self, quantity, max_speed, radius1, radius2):
        global all_balls
        all_balls = []
        for k in range(quantity):
            ball_0 = Ball(rnd(50, 750), rnd(50, 550), rnd(-max_speed, max_speed + 1), rnd(-max_speed, max_speed + 1), 0, 0, rnd(radius1, radius2 + 1) * (rnd(2, 5) // 2), 0)
            all_balls.append(ball_0)
    
    def global_movement(self, quantity, dt):
        global all_balls
        canv.delete(ALL)
        for k in range(quantity):
            for i in range(k):
                all_balls[k].collision(all_balls[i])
        for k in range(quantity):
            all_balls[k].wall_collision()
            all_balls[k].move_to(dt)
    
def update():
    global world, quantity, dt
    world.global_movement(quantity, dt)
    root.after(int(dt * 10000), update)



def main():
    global world, quantity, dt, canv
    
    canv = Canvas(root,bg='white')
    
    canv.pack(fill=BOTH,expand=1)
    
    dt = 0.001
    quantity = 50
    max_speed = 500
    radius1 = 10
    radius2 = 10
    
    world = World(dt)
    
    world.create_balls(quantity, max_speed, radius1, radius2)
    
    update()





mainloop()