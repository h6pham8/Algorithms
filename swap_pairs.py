"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
"""


def swap_pairs(head):
    counter = 0
    curr = head
    prev = None

    while curr:
        if not curr.next:
            return head

        hold = curr.next.next
        curr.next.next = curr

        # first node
        if counter == 0:
            counter += 1
            head = curr.next
        # reattach hook to previous
        else:
            prev.next = curr.next

        curr.next = hold
        prev = curr
        curr = curr.next

    return head
