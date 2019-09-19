#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_2_4():
    for k in range(5):
        move_right()
        fill_cell()
        move_down(1)
        fill_cell()
        move_right()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_up()        
        for i in range(9):
            move_right(5)
            fill_cell()
            move_down(1)
            fill_cell()
            move_right()
            fill_cell()
            move_down()
            move_left()
            fill_cell()
            move_left()
            move_up()
            fill_cell()
            move_up()
        move_left(36)
        if k == 4:
            move_up(4)
        move_down(4)


if __name__ == '__main__':
    run_tasks()
