#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
    move_right()
    for k in range(6):
        for i in range(13 - 2*k):
            move_down()
            fill_cell()
        move_right()
        fill_cell()
        for l in range(11 - 2*k):
            move_up()
            fill_cell()
        move_right()
    move_down()
    fill_cell()
    move_down()
    move_left(12)


if __name__ == '__main__':
    run_tasks()
