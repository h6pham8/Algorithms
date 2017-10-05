"""
Invert the tree given the root
"""


def invert_tree(root):

    if root:
        stack = [root]
    else:
        return root

    while len(stack) > 0:
        curr = stack.pop()

        hold = curr.left
        curr.left = curr.right
        curr.right = hold

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return root

