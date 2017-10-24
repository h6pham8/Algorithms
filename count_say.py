"""
1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
7.     13112221

1 is read off as 11
11 is read off as 21
21 is read off as 1211
"""
import unittest


def count_say(n):

    arr = [1]

    if n == 1:
        print "".join(map(str, arr))
        return "".join(map(str, arr))

    for i in range(1, n):
        replace_arr = []

        for idx, num in enumerate(arr):
            if idx == 0:
                curr = arr[0]
                counter = 1
                continue

            if num == curr:
                counter += 1
            else:
                replace_arr.append(counter)
                replace_arr.append(curr)
                curr = num
                counter = 1

        replace_arr.append(counter)
        replace_arr.append(curr)

        arr = replace_arr

    print "".join(map(str, arr))
    return "".join(map(str, arr))


class TestCountSay(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(count_say(1), '1')
        self.assertEqual(count_say(2), '11')
        self.assertEqual(count_say(7), '13112221')
        self.assertEqual(count_say(5), '111221')


if __name__ == "__main__":
    unittest.main()

