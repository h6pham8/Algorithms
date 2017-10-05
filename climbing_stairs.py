"""
You are climbing a stair case. it takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
import unittest


def climb_stairs(n):
    # n represents number of steps on the stairs

    prev_steps = {1: 1,
                  2: 2}

    if n not in prev_steps:
        prev_steps[n] = climb_stairs(n-1) + climb_stairs(n-2)

    return prev_steps[n]


class Test(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(5), 8)
        self.assertEqual(climb_stairs(1), 1)


if __name__ == '__main__':
    unittest.main()