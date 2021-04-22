"""
File: rocket.py
Name: Yunchuan Kao
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This function displays the rocket in any size
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def lower():
    """
    This function display the lower part of rocket's body
    """
    for i in range(SIZE):
        # Display '|' on the first column
        print('|', end='')
        for j in range(SIZE * 2):
            if j < SIZE:
                if j < i:
                    print('.', end='')
                else:
                    if SIZE % 2 == 1:
                        if (i + j) % 2 == 0:
                            print("\\", end='')
                        else:
                            print('/', end='')
                    else:
                        if (i + j) % 2 == 1:
                            print('/', end='')
                        else:
                            print("\\", end='')
            else:
                if SIZE % 2 == 1:
                    if (i + j) > SIZE * 2 - 1:
                        print('.', end='')
                    else:
                        if (i + j) % 2 == 0:
                            print("\\", end='')
                        else:
                            print('/', end='')
                else:
                    if (i + j) > SIZE * 2 - 1:
                        print('.', end='')
                    else:
                        if (i + j) % 2 == 1:
                            print('/', end='')
                        else:
                            print("\\", end='')
        # Display '|' on the last column
        print('|')


def upper():
    """
    This function display the upper part of rocket's body
    """
    for i in range(SIZE):
        # Display '|' on the first column
        print('|', end='')
        for j in range(SIZE * 2):
            # Divide two parts to execute codes by j == SIZE, here is left part(j<SIZE)
            if j < SIZE:
                if (i + j) < SIZE - 1:
                    print('.', end='')
                else:
                    # If SIZE is odd
                    if SIZE % 2 == 1:
                        if (i + j) % 2 == 0:
                            print('/', end='')
                        else:
                            print("\\", end='')
                    # If SIZE is even
                    else:
                        if (i + j) % 2 == 1:
                            print('/', end='')
                        else:
                            print("\\", end='')
            # Right part(j>=SIZE)
            else:
                if j > i + SIZE:
                    print('.', end='')
                else:
                    # If SIZE is odd
                    if SIZE % 2 == 1:
                        if (i + j) % 2 == 0:
                            print('/', end='')
                        else:
                            print("\\", end='')
                    # If SIZE is even
                    else:
                        if (i + j) % 2 == 1:
                            print('/', end='')
                        else:
                            print("\\", end='')
        # Display '|' on the last column
        print('|')


def belt():
    """
    This function display belts of the rocket
    """
    for i in range(SIZE * 2 + 1):
        if i == 0:
            print('+', end='')
        else:
            print('=', end='')
    print('+')


def head():
    """
    This function display the head of the rocket
    """
    # The SIZE in the first for loop stands for rows
    for i in range(SIZE):
        # (SIZE*2+2) stands for columns/ +2 means two blanks in the beginning and end respectively
        for j in range(SIZE * 2 + 2):
            # Because there is a blank at the beginning, it can be determined when to display '/' or '\' by j == SIZE
            if j <= SIZE:
                # Draw a form with i and j, then observe it → print out '/' if (i+j)>(SIZE-1)
                if (i + j) > SIZE - 1:
                    print('/', end='')
                else:
                    print(' ', end='')
            else:
                # Draw a form with i and j, then observe it → print out '\' if j<=(i+SIZE+1)
                if j <= (i + SIZE + 1):
                    print("\\", end='')
                else:
                    print(' ', end='')
        print(' ')

    # Another method
    # for i in range(1, SIZE+1):
    #     for j in range(SIZE+1-i, 0, -1):
    #         print(' ', end='')
    #     for k in range(i):
    #         print('/', end='')
    #     for m in range(i):
    #         print("\\", end='')
    #     for n in range(SIZE+1-i, 0, -1):
    #         print(' ', end='')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
