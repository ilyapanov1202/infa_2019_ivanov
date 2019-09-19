#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_5_10():
    fill_cell()
    while not wall_is_beneath():
        
        while not wall_is_on_the_right():
            move_right()
            fill_cell()
        move_down()
        fill_cell()
        while not wall_is_on_the_left():
            move_left()
            fill_cell()
            
            

if __name__ == '__main__':
    run_tasks()
