#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    n = 1
    while n == 1:
        n = 0
        while not wall_is_beneath():
            move_down()
            n = 1
        while wall_is_beneath() and not wall_is_on_the_right():
            move_right()
        while wall_is_beneath() and not wall_is_on_the_left():
            move_left()
        if not wall_is_beneath():
            n = 1
        
        

if __name__ == '__main__':
    run_tasks()
