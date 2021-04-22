"""
File: caesar.py
Name: Yunchuan Kao
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This function turns the ciphered word into the deciphered one
    """
    move_number = int(input('Secret number : '))
    old = input("What's the ciphered string? ")
    print('The deciphered string is: ' + deciphered(old, move_number))


def deciphered(old, move_number):
    """
    param old: int, the ciphered word user inputted
    param move_number: int, the number user inputted
    return: str, new
    """
    new = ''
    old = old.upper()
    for i in range(len(old)):
        # Find each letter of old in ALPHABET
        word = ALPHABET.find(old[i])
        # If word can be found in ALPHABET
        if word != -1:
            new_index = (word + move_number) % 26
            new_word = ALPHABET[new_index]
        # If word cannot be found in ALPHABET
        else:
            new_word = old[i]
        new += new_word
    return new


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
