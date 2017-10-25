"""
Given an integer n, return the number of trailing zeroes in n!.
"""
import unittest


def trailing_zeroes(num):
    final = factorial(num)
    count = 0
    flag = 1

    final_arr = list(map(int, str(final)))
    print final_arr
    while flag:
        check = final_arr.pop()
        if check == 0:
            count += 1
        else:
            flag = 0

    return count


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class TestTrailingZeroes(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(trailing_zeroes(3), 0)
        self.assertEqual(trailing_zeroes(10), 2)
        self.assertEqual(trailing_zeroes(17), 3)


if __name__ == '__main__':
    unittest.main()