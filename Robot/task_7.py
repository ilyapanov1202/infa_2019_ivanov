#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.01)
def task_5_4():
    n = 0
    while wall_is_beneath() == 0:
        move_down()
    while wall_is_beneath():
        move_right()
        n += 1
    move_down()
    for k in range(n):
        move_left()
    
if __name__ == '__main__':
    run_tasks()
