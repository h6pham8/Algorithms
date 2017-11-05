"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
"""


def find_repeat_dna_seq(s):

    arr = []
    duplicate_check = {}
    final = []

    stop_length = len(s) - 9
    for idx in range(0, stop_length):
        word = ''
        for get_ten in range(0, 10):
            word = word + s[idx + get_ten]
        arr.append(word)

    for check in arr:
        if check in duplicate_check:
            if duplicate_check[check] == 0:
                final.append(check)
                duplicate_check[check] += 1
        else:
            duplicate_check[check] = 0

    return final
