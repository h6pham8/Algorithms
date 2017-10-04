"""
Given: two strings s and t which consist of only lowercase letters
Objective: find the letter that was added in t
Return: str
"""


def find_difference(s, t):

    arr_s = list(s)
    arr_t = list(t)

    hash_s = {}

    for letter in arr_s:
        if letter in hash_s:
            hash_s[letter] += 1
        else:
            hash_s[letter] = 1

    for letter in arr_t:
        if letter in hash_s:
            hash_s[letter] -= 1
        else:
            return letter

    for key in hash_s:
        if hash_s[key] < 0:
            return key
