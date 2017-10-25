"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""
import unittest


def judge_circle(seq):
    val = {"U": 1, "D": -1, "L": -1, "R": 1}
    left_right = 0
    up_down = 0
    
    for direction in seq:
        if direction is "U" or "D":
            up_down += val[direction]
        else:
            left_right += val[direction]
            
    if up_down == 0 and left_right == 0:
        return True
    else:
        return False


class TestJudgeRoute(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(judge_circle("UD"), True)
        self.assertEqual(judge_circle("LL"), False)
        self.assertEqual(judge_circle("URDL"), True)
        

if __name__ == "__main__":
    unittest.main()