"""
File: hangman.py
Name: Yunchuan Kao
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function plays the hangman game and user needs to find the correct word
    """
    vol = random_word()
    # Create a 'fail' variable to record the number of wrong guesses
    fail = 0
    # Create an empty 'guess' as the original guess when user hasn't guessed
    guess = ''
    # Create an empty 'store' to store the correct strings
    store = ''
    store = word_show(vol, guess, store)
    print('The word looks like: ' + store)
    print('You have ' + str(N_TURNS - fail) + ' guesses left.')
    guess = input('Your guess: ').upper()
    while N_TURNS-fail > 0:
        # Whether the letter user guessed is alphabet
        if guess.isalpha():
            # Whether the length of letters user inputted is over 1
            if len(guess) > 1:
                print('Illegal format.')
                guess = input('Your guess: ')
            else:
                # If 'guess' can be found in random word
                if vol.find(guess) != -1:
                    print('You are correct!')
                    store = word_show(vol, guess, store)
                    print('The word looks like: ' + store)
                    print('You have ' + str(N_TURNS - fail) + ' guesses left.')
                    guess = input('Your guess: ').upper()
                else:
                    print('There is no ' + guess + "'s in the word.")
                    # Count the number of failure
                    fail += 1
                    # Create a list of hangman pictures
                    pic = ["""
                                        ------
                                        |  | 
                                        |
                                        |
                                        |
                                        """, """
                                        ------
                                        |  | 
                                        |  0
                                        |
                                        |
                                        """, """
                                        ------
                                        |  | 
                                        |  0
                                        |  |
                                        |
                                        """, """
                                        ------
                                        |  | 
                                        |  0
                                        | /|
                                        |
                                        """, """
                                        ------
                                        |  | 
                                        |  0
                                        | /|\\
                                        |
                                        """, """
                                        ------
                                        |  | 
                                        |  0
                                        | /|\\
                                        | /
                                        """, """
                                        ------
                                        |  | 
                                        |  0
                                        | /|\\
                                        | / \\
                                        """]
                    # Showing the certain hangman picture according to failure times
                    print(pic[fail - 1])
                    print('The word looks like: ' + store)
                    if N_TURNS == fail:
                        break
                    else:
                        print('You have ' + str(N_TURNS - fail) + ' guesses left.')
                        guess = input('Your guess: ').upper()
        else:
            print('Illegal format.')
            guess = input('Your guess: ').upper()
        store = word_show(vol, guess, store)
        # If there is no '-' in stored word
        if store.find('-') == -1:
            print('You win!! \nThe word was: '+vol)
            break
    # If the number of failure is equals to N_TURNS, user loses the game
    if fail == N_TURNS:
        print('You are completely hung :( \nThe word was: ' + vol)


def word_show(vol, guess, store):
    """
    param vol: str, the word from def random_word
    param guess: str, the letter user guessed
    param store: str, the string showing correct letters user guessed
    return: str, answer
    """
    answer = ''
    if guess == '':
        for i in vol:
            answer += '-'
    else:
        for j in range(len(vol)):
            if guess == vol[j]:
                answer += guess
            else:
                answer += store[j]
    return answer


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
