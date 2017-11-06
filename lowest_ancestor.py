"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w
as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.
"""


def lowest_ancestor(root, p, q):

    stack = [(root, 0)]
    pathing = []
    found = 0

    while stack:
        curr = stack.pop()
        if found == 0:
            pathing.insert(curr[1], curr[0])
        else:
            pathing.insert(curr[1], 'x')

        if curr[0] == p or curr[0] == q:
            if found == 0:
                found = 1
            else:
                for idx, val in enumerate(pathing):
                    if val == 'x':
                        return pathing[idx - 1]

        if curr[0].left:
            stack.append((curr[0].left, curr[1] + 1))
        if curr[0].right:
            stack.append((curr[0].right, curr[1] + 1))
