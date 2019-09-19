#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_5_2():
    while wall_is_beneath():
        move_right()


if __name__ == '__main__':
    run_tasks()
