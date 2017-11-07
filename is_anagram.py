"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""
import unittest


def is_anagram(s, t):
    letters_s = {}
    letters_t = {}

    for letter in s:
        if letter in letters_s:
            letters_s[letter] += 1
        else:
            letters_s[letter] = 1

    for letter in t:
        if letter in letters_t:
            letters_t[letter] += 1
        else:
            letters_t[letter] = 1

    return letters_s == letters_t


class TestAnagram(unittest.TestCase):
    def test_cases(self):
        self.assertFalse(is_anagram('rat', 'car'))
        self.assertTrue(is_anagram('what', 'thwa'))


if __name__ == '__main__':
    unittest.main()