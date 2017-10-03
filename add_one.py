'''
Given: non-negative integer represented as a non-empty array of digits

Objective: plus one to the integer

Return: List[int]
'''


import unittest

def plus_one(num):

    rev = num[::-1]
    carry = 0

    for idx, digit in enumerate(rev):
        if idx == 0 or carry == 1:
            rev[idx] += 1

        if rev[idx] == 10:
            carry = 1
            rev[idx] = 0
        else:
            carry = 0

    if carry == 1:
        rev.append(1)

    return rev[::-1]


class TestFunction(unittest.TestCase):
    def test_plus_one(self):
        case = [1, 0, 9, 9, 9]
        expected = [1, 1, 0, 0, 0]
        self.assertEqual(plus_one(case), expected)

        case = [9]
        expected = [1, 0]
        self.assertEqual(plus_one(case), expected)

