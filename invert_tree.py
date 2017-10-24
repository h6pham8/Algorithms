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

def invert_tree_recursive(root):

    if root:
        curr = root
    else:
        return root

    hold = curr.left
    curr.left = curr.right
    curr.right = hold

    if curr.left:
        invert_tree_recursive(curr.left)
    if curr.right:
        invert_tree_recursive(curr.right)

