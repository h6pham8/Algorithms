"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
import unittest


def contains_duplicate(arr):
    mem = {}

    for num in arr:
        if num in mem:
            return True
        else:
            mem[num] = 1

    return False


class TestDuplicate(unittest.TestCase):
    def test_case(self):
        self.assertEqual(contains_duplicate([1]), False)
        self.assertEqual(contains_duplicate([1, 1]), True)
        self.assertEqual(contains_duplicate([1, 2, 3, 4]), False)
        self.assertEqual(contains_duplicate([1, 2, 3, 4, 1]), True)
        
        
if __name__ == "__main__":
    unittest.main()