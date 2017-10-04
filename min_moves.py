"""
Objective: given a non-empty integer arr of size n, find the minimum number of moves to make all arr elements equal
Return: List[int]
"""

def min_moves(nums):

    moves = 0

    while min(nums) != max(nums):

        max_value = max(nums)
        max_index = nums.index(max_value)

        for idx, num in enumerate(nums):
            if idx != max_index:
                nums[idx] += 1

        moves += 1

    print moves
    return moves


