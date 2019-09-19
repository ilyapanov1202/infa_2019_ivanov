#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    fill_cell()
    v = 0
    ax = 0
    while wall_is_above() or wall_is_on_the_left() or wall_is_beneath():
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                v += 1
            fill_cell()
        while not wall_is_beneath():
            move_down()
        if not wall_is_on_the_right() and wall_is_beneath():
            move_right()
            while not wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
                fill_cell()
                move_right()
    mov('ax', v)
if __name__ == '__main__':
    run_tasks()
