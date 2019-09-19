#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_29():
    while wall_is_on_the_left() == 0 and wall_is_above():
        move_left()
    while wall_is_on_the_right() == 0 and wall_is_above():
        move_right()
    if wall_is_above():
        pass
    else:
        while wall_is_above() == 0:
            move_up()
        while wall_is_on_the_left() == 0:
            move_left()


if __name__ == '__main__':
    run_tasks()
