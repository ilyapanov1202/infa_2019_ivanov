#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_2_1():
    move_right(2)
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


if __name__ == '__main__':
    run_tasks()
