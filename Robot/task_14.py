#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_11():
    while wall_is_on_the_right() == 0:
        if wall_is_above() == 0:
            move_up()
            fill_cell()
            move_down()
        if wall_is_beneath() == 0:
            move_down()
            fill_cell()
            move_up()
        if wall_is_beneath() and wall_is_above():
            fill_cell()
        move_right()
    if wall_is_above() == 0:
        move_up()
        fill_cell()
        move_down()
    if wall_is_beneath() == 0:
        move_down()
        fill_cell()
        move_up()
    if wall_is_beneath() and wall_is_above():
        fill_cell()

if __name__ == '__main__':
    run_tasks()
