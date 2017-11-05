"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""


def num_squares(n):
    
    if n == 0:
        return 0

    layer = 0
    check = [n]
    roots = []
    counter = 1
    while pow(counter, 2) <= n:
        roots.append(pow(counter, 2))
        counter += 1

    while True:
        next_layer = []
        layer = layer + 1
        for num in check:
            for root in roots:
                if root <= num:
                    diff = num - root
                    if diff == 0:
                        return layer
                    else:
                        next_layer.append(diff)
        check = next_layer
