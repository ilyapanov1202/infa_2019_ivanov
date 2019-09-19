#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    n = 1
    while not wall_is_on_the_right():
        move_right()
        n += 1
    move_left(n-2)
    for k in range((n-2+1)//2):
        fill_cell()
        for i in range(n-2-1-2*k):
            move_right()
            fill_cell()
        move_down()
        move_left(abs(n-2-2*(k+1)))
    move_right(n//2 + 1)
    move_up(n//2 - 1)
    for k in range((n-2+1)//2):
        fill_cell()
        for i in range(n-2-1-2*k):
            move_down()
            fill_cell()
        move_left()
        move_up(abs(n-2-2*(k+1)))   
    move_down(n//2 + 1)
    move_right(n//2 - 1)
    for k in range((n-2+1)//2):
        fill_cell()
        for i in range(n-2-1-2*k):
            move_left()
            fill_cell()
        move_up()
        move_right(abs(n-2-2*(k+1)))
    move_left(n//2 + 1)
    move_down(n//2 - 1)
    for k in range((n-2+1)//2):
        fill_cell()
        for i in range(n-2-1-2*k):
            move_up()
            fill_cell()
        move_right()
        move_down(abs(n-2-2*(k+1)))   
    move_down(n//2 - 1)
    move_left(n//2)



if __name__ == '__main__':
    run_tasks()
