"""
File: similarity.py
Name: Yunchuan Kao
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""
"""
FOR TEST
actgacattg/ atcgatCGATcgc
tgcca/ tcGC
"""


def main():
    """
    This function compares the short DNA sequence with the long one and find the highest similarity in long sequence
    """
    long = input('Please give me a DNA sequence: ')
    short = input('What DNA sequence would you like to match? ')
    print('The best match is ' + similarity(long, short))


def similarity(long, short):
    """
    param long: str, the DNA sequence user inputted
    param short: str, the DNA sequence user wanted to match
    return: str, homology
    """
    long = long.upper()
    short = short.upper()
    len_short = len(short)
    homology = ''
    # Create a variable to record the best match
    maximum = 0
    for i in range(len(long)-len_short+1):
        # Create the same length of short sequence in the long sequence to compare the similarity
        group = long[i:i+len_short]
        # Create a variable to count the the number where the short letter matches the long one
        count = 0
        for j in range(len(short)):
            s1 = group[j]
            s2 = short[j]
            # If the letters are the same, add a count
            if s1 == s2:
                count += 1
        # Find the maximum count
        if count > maximum:
            maximum = count
            # Extract the string that has highest count
            homology = group
    return homology


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
