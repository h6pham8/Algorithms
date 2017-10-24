"""
Find the contiguous subarray within an array which has the largest sum.

Ex:

Given the array [-2, 1, -3, 4, -1, 2, 1, -5 ,4]
The contiguous subarray [4, -1, 2, 1] has the largest sum = 6
"""


def max_sub_arr(nums):

    if nums:
        sum_prev = [nums[0]]
    else:
        return None

    for idx in range(1, len(nums)):
        sum_prev.append(sum_prev[idx-1] + nums[idx])

    print max(sum_prev) - min(sum_prev)


max_sub_arr([-2, 1, -3, 4, -1, 2, 1, -5, 4])

