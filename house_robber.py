"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is
that adjacent houses have security system connected and it will automatically contact the police if two adjacent
 houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.
"""
import unittest


def house_robber(arr):

    a = 0
    b = 0

    for i in range(0, len(arr)):
        if i % 2 == 0:
            a = max(a + arr[i], b)
        else:
            b = max(b + arr[i], a)

    return max(a, b)


class TestHouseRobber(unittest.TestCase):
    def test_choice(self):
        self.assertEqual(house_robber([5, 6, 30, 1]), 35)
        self.assertEqual(house_robber([5, 5, 5, 5]), 10)
        self.assertEqual(house_robber([100, 1, 1, 100]), 200)
        self.assertEqual(house_robber([100, 1, 1, 1, 100]), 201)
        self.assertEqual(house_robber([100, 1, 51, 100, 51]), 202)
        self.assertEqual(house_robber([100]), 100)


if __name__ == '__main__':
    unittest.main()
