'''
Given: input string
Objective: reverse the string word by word
Return: str
'''


import unittest


def reverse_words(s):

    space_remove = s.split()
    rev = space_remove[::-1]

    final = ' '.join(rev)

    print final

    return final


class Test(unittest.TestCase):

    def test_reverse_words(self):
        case = 'hello how are you doing'
        expect = 'doing you are how hello'
        self.assertEquals(reverse_words(case), expect)

