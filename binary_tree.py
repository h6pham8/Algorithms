"""
Implementation of a binary tree with all available features
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)

        if self.root:
            parent, current = self.root, self.root

            while current is not None:
                if new_node.value > current.value:
                    parent = current
                    current = current.right
                else:
                    parent = current
                    current = current.left

            if parent.value > new_node.value:
                parent.left = new_node
            else:
                parent.right = new_node

        else:
            self.root = new_node

    # this function will print out a serialized form of the binary tree
    # for simplicity the 0 index of the array will be unused
    # root index = 1
    # left child = 2 * parent index
    # right child = 2 * parent index + 1
    # [ 0, 1(root), 2(left child), 3(right child), 4(left child of left child) ... etc ]
    def serialize(self):
        arr = [0]

        # implement bfs
        queue = [self.root]

        while queue:
            curr = queue.pop()
            if curr is not None:
                arr.append(curr.value)
            else:
                arr.append(None)
                continue

            if curr.left is not None:
                queue.insert(0, curr.left)
            else:
                queue.insert(0, None)

            if curr.right is not None:
                queue.insert(0, curr.right)
            else:
                queue.insert(0, None)

        print arr


b = BinaryTree()
b.insert(10)
b.insert(1)
b.insert(13)
b.insert(4)
b.insert(5)
b.serialize()


