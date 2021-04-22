from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Yunchuan Kao
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Pre-condition:Karel is at the northwest side of the house, facing East
    Post-condition:Karel comes back to the same place in the house and puts down the newspaper, facing East
    """
    move_to_newspaper()
    pick_and_move()


def turn_around():
    turn_left()
    turn_left()


def pick_and_move():
    """
    Pre-condition:Karel is on the newspaper, facing East
    Post-condition:Karel comes back to the same place in the house and puts down the newspaper, facing East
    """
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def move_to_newspaper():
    """
    Pre-condition:Karel is at the northwest side of the house, facing East
    Post-condition:Karel is on the newspaper, facing East
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
