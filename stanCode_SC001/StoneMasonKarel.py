from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Yunchuan Kao
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Pre-condition:Karel is at the right side of the wall, facing East
    Post-condition:Karel stops at street 1, left side of the wall, facing East
    """
    start()
    while right_is_clear():
        process()
    end()


def end():
    """
    Pre-condition:Karel is at the left side of the wall, facing North
    Post-condition:Karel stops at street 1, left side of the wall, facing East
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_around()
    move_to_the_end()
    turn_left()


def process():
    """
    Pre-condition:Karel is at the next pillar, facing North
    Post-condition:Karel is at the left side of the wall, facing North
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_around()
    move_to_the_end()
    turn_left()
    move_forward()
    turn_left()


def start():
    """
    Pre-condition:Karel is at the right side of the wall, facing East
    Post-condition:Karel is at the next pillar, facing North
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    turn_around()
    move_to_the_end()
    turn_left()
    move_forward()
    turn_left()


def move_to_the_end():
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


def move_forward():
    """
    Pre-condition:Karel is at street 1, facing East
    Post-condition:Karel moves four steps
    """
    for i in range(4):
        move()


def turn_right():
    for i in range(3):
        turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
