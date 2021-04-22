from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Yunchuan Kao
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    Pre-condition:Karel is at (1, 1), facing East
    Post-condition:Karel is at the last top of the avenue, facing North
    """
    fill_in_avenue_1()
    fill_in_street_1()
    while right_is_clear():
        process()
    stop()


def stop():
    """
    Pre-condition:Karel fills in the last avenue, whose right side is clear, facing North
    Post-condition:Karel is at the last top of the avenue, facing North
    """
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
            if front_is_clear():
                move()
        else:
            move()
            if front_is_clear():
                move()
                put_beeper()


def process():
    """
    Pre-condition:Karel is at (1, 2), facing North
    Post-condition:Karel fills in the last avenue, whose right side is clear, facing North
    """
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
            if front_is_clear():
                move()
        else:
            move()
            if front_is_clear():
                move()
                put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    move()
    turn_left()


def fill_in_street_1():
    """
    Pre-condition:Karel fills in the Avenue 1, at (1, 1) or (1, 2), facing East
    Post-condition:Karel is at (1, 2), facing North
    """
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
            if front_is_clear():
                move()
        else:
            move()
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    if front_is_clear():
        move()
        turn_left()


def fill_in_avenue_1():
    """
    Pre-condition:Karel is at (1, 1), facing East
    Post-condition:Karel fills in the Avenue 1, at (1, 1) or (1, 2), facing East
    """
    put_beeper()
    turn_left()
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
            if front_is_clear():
                move()
        else:
            move()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)