'''
Given: arr of size n

Objective: find the majority element. Majority element is the element that appears more than [n / 2] times.

Return: int
'''


import unittest


def majority_element(nums):

    # need a way to keep track of count of numbers
    dict = {}

    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

        if dict[num] > len(nums) / 2:
            return num


class MyTest(unittest.TestCase):
    def test(self):
        func = majority_element([1, 0, 10, 3, 2, 3, 3, 3, 3])
        self.assertEqual(func, 3)
