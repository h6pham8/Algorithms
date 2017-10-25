"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100"
"""
import unittest


def add_binary(a, b):
    a = list(a)
    b = list(b)
    final = []
    carry = 0

    while a or b:
        if a:
            digit_a = a.pop()
        else:
            digit_a = 0

        if b:
            digit_b = b.pop()
        else:
            digit_b = 0

        tot = int(digit_a) + int(digit_b) + carry
        if tot == 2:
            carry = 1
            tot = 0
        elif tot == 3:
            carry = 1
            tot = 1
        else:
            carry = 0

        final.insert(0, str(tot))

    if carry == 1:
        final.insert(0, str(carry))

    final = "".join(final)

    return final



class TestAddBinary(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(add_binary("11", "1"), "100")
        self.assertEqual(add_binary("1", "0"), "1")
        self.assertEqual(add_binary("111", "111"), "1110")


if __name__ == '__main__':
    unittest.main()