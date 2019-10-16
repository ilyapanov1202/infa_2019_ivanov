'''GAME RULES:
1. Goal of the game is to score maximum points
2. The game ends when you score 5 penalty points
3_1. For hitting the center of a colored target you get 5 points
3_2. For hitting the colored part of the target you get 2 points
3_3. For hitting the nearby area you get 1 point
4. For a miss you get a penalty point
5. Hitting a black bomb immediately leads to defeat, you get 10 penalty points
6. When you get points, the target accelerates
7. Over time the target slows down
8. The target bounces off the walls at a random angle
9. You have 30 sec per game

Play this game and find out the truth about yourself!
'''






from tkinter import *

from random import randrange as rnd, choice

import time

root = Tk()

root.geometry('800x600')

canv = Canvas(root,bg='white')

canv.pack(fill=BOTH,expand=1)

l = Label(root, text = "score", bg = "black", fg = "white", font = "Arial 36", width = 7)
l.place(relx = 0, rely = 0)

l2 = Label(root, text = "penalties", bg = "black", fg = "white", font = "Arial 36", width = 10)
l2.place(relx = 0.65, rely = 0)

l3 = Label(root, bg = "black", fg = "white", font = "Arial 36", width = 4)
l3.place(relx = 0.4, rely = 0)





colors = ['red','orange','yellow','green','blue']

def new_goal(x, y, r):

	b1 = new_ball_color(x, y, r, "white")

	b2 = new_ball(x, y, r / 3 * 2)

	b3 = new_ball(x, y, r / 3)

	return [b1, b2, b3]



def rnd_goal():
	
	global a2, b2, c2
	
	a2, b2, c2 = rnd(100, 700), rnd(100, 500), rnd(50, 100)
	return new_goal(a2, b2, c2)

	

def rnd_ball():

	return new_ball(rnd(100, 700), rnd(100, 500), rnd(50, 100))



def new_ball(x, y, r):
	global a1, b1, c1
	
	ball = dict()

	ball['x'] = x 

	ball['y'] = y 

	ball['r'] = r 

	ball['o'] = canv.create_oval(x-r,y-r,x+r,y+r,

			fill=choice(colors), width=0)
	
	a1, b1, c1 = x, y, r
	return ball


def new_ball_color(x, y, r, color):
	global a1, b1, c1
	
	ball = dict()

	ball['x'] = x 

	ball['y'] = y 

	ball['r'] = r 

	ball['o'] = canv.create_oval(x-r,y-r,x+r,y+r,

			fill=color, width=0)
	
	a1, b1, c1 = x, y, r
	return ball


counter = 0
flag = 0
def click(event):
	global counter, flag
	if (a2 - event.x) ** 2 + (b2 - event.y) ** 2 < (c2 / 3) ** 2:
		print("+5 points")
		counter += 5
		l['text'] = ''.join("score:" + str(counter))
	elif (a2 - event.x) ** 2 + (b2 - event.y) ** 2 < (c2 / 3 * 2) ** 2:
		print("+2 points")
		counter += 2
		l['text'] = ''.join("score:" + str(counter))
	elif (a2 - event.x) ** 2 + (b2 - event.y) ** 2 < c2 ** 2:
		print("+1 point")
		counter += 1
		l['text'] = ''.join("score:" + str(counter))	
		
	else:
		print("miss", int((a2 - event.x) ** 2 + (b2 - event.y) ** 2 - c2 ** 2))
		if counter > 0:
			counter -= 1
			l['text'] = ''.join("score:" + str(counter))
		flag += 1
		l2['text'] = ''.join("penalties:" + str(flag))
			
	if (a1 - event.x) ** 2 + (b1 - event.y) ** 2 < c1 ** 2:
		if counter > 10:
			print("-10 points")
			counter += -10
			l['text'] = ''.join("score:" + str(counter))
		elif counter > 0:
			print("-", counter, " points", sep = "")
			counter = 0
			l['text'] = ''.join("score:" + str(counter))
		flag += 10
		l2['text'] = ''.join("penalties:" + str(flag))
	
	if flag >= 5:
		end_game()



def move_ball(ball, dx, dy):

	ball['x'] += dx

	ball['y'] += dy

	canv.move(ball['o'], dx, dy)



def move_goal(goal, dx, dy):
	
	for ball in goal:

		move_ball(ball, dx, dy)


move_x2, move_y2 = 5, 5
move_x1, move_y1 = 3, 3

def update():
	global a2, b2, a1, b1, move_x2, move_y2, move_x1, move_y1, counter, timer_default, timer_on
	timer_on = time.time()
	l3['text'] = ''.join(str(int(30 - (timer_on - timer_default))))
	if timer_on - timer_default > 30:
		end_game()
	
	if (a2 < c2 and move_x2 < 0) or (800 - a2 < c2 and move_x2 > 0):
		move_x2 = -move_x2 * rnd(7, 13) / 10
	if (b2 - 60 < c2 and move_y2 < 0) or (600 - b2 < c2 and move_y2 > 0):
		move_y2 = -move_y2 * rnd(7, 13) / 10
	
		
	a2 += move_x2 * 2 ** (counter/50)
	b2 += move_y2 * 2 ** (counter/50)
	
	if (a1 < c1 and move_x1 < 0) or (800 - a1 < c1 and move_x1 > 0):
		move_x1 = -move_x1 * rnd(7, 13) / 10
	if (b1 - 60 < c1 and move_y1 < 0) or (600 - b1 < c1 and move_y1 > 0):
		move_y1 = -move_y1 * rnd(7, 13) / 10
	
		
	
	a1 += move_x1 * 2 ** (counter/50)
	b1 += move_y1 * 2 ** (counter/50)
	
	move_goal(goal2, move_x2 * 2 ** (counter/50), move_y2 * 2 ** (counter/50))
	move_ball(bomb_1, move_x1 * 2 ** (counter/50), move_y1 * 2 ** (counter/50))
	
	root.after(10, update)

def end_game():
	global counter
	canv.delete(ALL)
	l2 = Label(text = "Length of your dick:" + str(counter) + "cm", font = "Arial 46 bold", height = 9, width = 22)
	l2.place(relx=0, rely=0)

timer_default = time.time()

goal2 = rnd_goal()

bomb_1 = new_ball_color(50, 50, 50, "black")

update()

canv.bind('<Button-1>', click)

mainloop()