#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_2_2():
    move_right()
    move_down(1)
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
    for i in range(4):
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
        


if __name__ == '__main__':
    run_tasks()
