#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_3_3():
    if wall_is_above() != True:
        move_up()
    elif wall_is_beneath() != True:
        move_down()
    elif wall_is_on_the_left() != True:
        move_left()
    else:
        move_right()

if __name__ == '__main__':
    run_tasks()
