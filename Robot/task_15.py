#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_21():
    if wall_is_above():
        if wall_is_on_the_left():
            while wall_is_on_the_right() == 0:
                move_right()
            while wall_is_beneath() == 0:
                move_down()
        elif wall_is_on_the_right():
            while wall_is_on_the_left() == 0:
                move_left()
            while wall_is_beneath() == 0:
                move_down()        
    elif wall_is_beneath():
        if wall_is_on_the_left():
            while wall_is_on_the_right() == 0:
                move_right()
            while wall_is_above() == 0:
                move_up()
        elif wall_is_on_the_right():
            while wall_is_on_the_left() == 0:
                move_left()
            while wall_is_above() == 0:
                move_up()       

if __name__ == '__main__':
    run_tasks()
