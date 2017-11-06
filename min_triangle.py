"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""


def min_triangle(triangle):

    if not triangle:
        return None

    for idx_x, x in enumerate(triangle):
        # skip first row since there are no computations
        if idx_x == 0:
            continue
        for idx_y, y in enumerate(x):
            # check if it is a corner
            if idx_y == 0 or idx_y == (len(triangle[idx_x]) - 1):
                triangle[idx_x][idx_y] = calc_edge(idx_x, idx_y, triangle)
            # middle
            else:
                triangle[idx_x][idx_y] = calc_middle(idx_x, idx_y, triangle)

    return min(triangle[len(triangle) - 1])


def calc_middle(idx_x, idx_y, triangle):
    tot = triangle[idx_x][idx_y]
    if triangle[idx_x - 1][idx_y] <= triangle[idx_x - 1][idx_y - 1]:
        tot += triangle[idx_x - 1][idx_y]
    else:
        tot += triangle[idx_x - 1][idx_y - 1]

    return tot


def calc_edge(idx_x, idx_y, triangle):
    tot = triangle[idx_x][idx_y]
    if idx_y == 0:
        tot += triangle[idx_x - 1][idx_y]
    elif idx_y == (len(triangle[idx_x]) - 1):
        tot += triangle[idx_x - 1][len(triangle[idx_x - 1]) - 1]

    return tot

