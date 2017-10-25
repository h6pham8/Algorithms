"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the tot of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
import unittest


def is_happy(num):

    repeat_check = {}
    num_arr = list(map(int, str(num)))

    while(True):
        tot = 0

        for num in num_arr:
            tot += pow(num, 2)

        if tot in repeat_check:
            return False
        elif tot == 1:
            return True
        else:
            repeat_check[tot] = 1
            num_arr = list(map(int, str(tot)))


class TestHappyNumber(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_happy(19), True)
        self.assertEqual(is_happy(5), False)
        self.assertEqual(is_happy(12), False)
        self.assertEqual(is_happy(13), True)
        self.assertEqual(is_happy(1), True)
        self.assertEqual(is_happy(0), False)


if __name__ == '__main__':
    unittest.main()