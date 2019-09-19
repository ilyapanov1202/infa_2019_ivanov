#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_28():
    flag = 0
    while wall_is_on_the_left() == 0:
        if wall_is_above() == 0:
            move_up()
            flag = 1
            break
        move_left()
    if flag == 0:
        while wall_is_on_the_right() == 0:
            if wall_is_above() == 0:
                move_up()
                break
            move_right()
    else:
        pass
    while wall_is_above() == 0:
        move_up()
    while wall_is_on_the_left() == 0:
        move_left()

if __name__ == '__main__':
    run_tasks()
