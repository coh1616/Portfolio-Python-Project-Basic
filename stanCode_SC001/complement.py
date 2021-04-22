"""
File: complement.py
Name: Yunchuan Kao
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This function turns the given strand of DNA into a complement of that strand of DNA(case-insensitive)
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    complement_dna = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(complement_dna))


def build_complement(dna):
    complement_dna = ''
    strand = dna.upper()
    for i in strand:
        if i == 'A':
            complement_dna += 'T'
        elif i == 'T':
            complement_dna += 'A'
        elif i == 'C':
            complement_dna += 'G'
        elif i == 'G':
            complement_dna += 'C'
    return complement_dna


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
