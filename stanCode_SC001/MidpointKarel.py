from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Yunchuan Kao
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Pre-condition:Karel is at (1, 1), facing East
    Post-condition:Karel is at the middle of Street 1 and put a beeper
    """
    if front_is_clear():
        start_and_end_without_beeper()
        collect_beepers()
        move_to_beeper()
    put_beeper()


def collect_beepers():
    """
    Pre-condition:Karel is at the end of Street 1, facing West
    Post-condition:Karel is at the left/ right side of the wall, facing East/ West
    """
    while front_is_clear():
        move()
        if on_beeper():
            move()
            if on_beeper():
                turn_around()
                move()
                pick_beeper()
                turn_around()
                move_to_the_end()
    turn_around()


def start_and_end_without_beeper():
    """
    Pre-condition:Karel is at (1, 1), facing East
    Post-condition:Karel is at the end of Street 1, facing West
    """
    while front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
    pick_beeper()
    turn_around()

    # or maintain original
    # def main():
    #     start_and_end_without_beeper()
    #     collect_beepers()
    #     move_to_beeper()
    #     put_beeper()
    #
    # then change
    # def start_and_end_without_beeper():
    # while front_is_clear():
    #     move()
    #     if not on_beeper():
    #         put_beeper()
    # Change this part
    # if on_beeper():
    #     pick_beeper()
    #     turn_around()
    # however, add if front_is_clear() in def main() is much better because the it will not execute redundant code


def move_to_the_end():
    while front_is_clear():
        move()
    turn_around()


def move_to_beeper():
    """
    Pre-condition:Karel is at the left/ right side of the wall, facing East/ West
    Post-condition:Karel moves to the only beeper and pick it
    """
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            # Turn to the side that front isn't clear, then it can jump out of the loop and move to next code
            if facing_east():
                turn_right()
            if facing_west():
                turn_left()
    # Original wrong code
    # while not on_beeper():
    #     if front_is_clear():
    #         move()
    #     else:
    #         turn_around()
    # pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()
# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
