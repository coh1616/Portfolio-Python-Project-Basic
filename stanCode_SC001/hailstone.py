"""
File: hailstone.py
Name: Yunchuan Kao
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences
    """
    print('This program computes Hailstone sequences.')
    number = int(input('Enter a number: '))
    # Set a variable to count how many steps it took to reach 1
    step = 0
    while number != 1:
        step += 1
        if number % 2 == 1:
            odd_way = 3 * number + 1
            print(str(number) + ' is odd, so I make 3n+1: ' + str(odd_way))
            number = odd_way
        else:
            even_way = int(number / 2)
            print(str(number) + ' is even, so I take half: ' + str(even_way))
            number = even_way
    print('It took ' + str(step) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
