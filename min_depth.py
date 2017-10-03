'''
Given: Root of a tree
Objective: determine the minimum depth of the tree
Return: int
'''


def min_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if root:
        queue = [root]
        node_depth = [1]
    else:
        return 0

    while True:
        curr = queue.pop()
        curr_depth = node_depth.pop()

        if curr.left is None and curr.right is None:
            return curr_depth

        if curr.left:
            queue.insert(0, curr.left)
            node_depth.insert(0, curr_depth + 1)

        if curr.right:
            queue.insert(0, curr.right)
            node_depth.insert(0, curr_depth + 1)


