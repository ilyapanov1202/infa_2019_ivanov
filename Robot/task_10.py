#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_3():
    while wall_is_on_the_right() == 0:
        if wall_is_above() or wall_is_beneath():
            fill_cell()
        move_right()
    if wall_is_above() or wall_is_beneath():
        fill_cell()


if __name__ == '__main__':
    run_tasks()
