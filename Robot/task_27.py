#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_5():
    n = 0
    k = 0
    while not wall_is_on_the_right():
        move_right()
        if wall_is_on_the_right():
            break
        if k == n:
            fill_cell()
            n += 1
            k = 0
        k += 1


if __name__ == '__main__':
    run_tasks()
