"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
import unittest


def title_to_num(col):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
            'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    digit_place = 0
    col = list(col)
    tot = 0

    while col:
        letter = col.pop()
        tot += pow(26, digit_place) * alphabet[letter]
        digit_place += 1

    return tot


class TestExcelSheet(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(title_to_num('A'), 1)
        self.assertEqual(title_to_num('AA'), 27)
        self.assertEqual(title_to_num('Z'), 26)
        self.assertEqual(title_to_num('ZZ'), 702)
        self.assertEqual(title_to_num('ZAZC'), 458331)


if __name__ == '__main__':
    unittest.main()