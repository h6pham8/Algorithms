"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit
"""
import unittest

def add_digits(num):

    # turn num into an arr of num
    arr_num = [int(i) for i in str(num)]

    while len(arr_num) != 1:
        tot = sum(arr_num)
        arr_num = [int(i) for i in str(tot)]

    arr_num = ''.join(map(str, arr_num))

    print arr_num
    return int(arr_num)


class Test(unittest.TestCase):
    def test_add_dig(self):
        self.assertEqual(add_digits(38), 2)

if __name__ == '__main__':
    unittest.main()