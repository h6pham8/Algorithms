"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""


def reorder(head):
    if not head:
        return

    slow, curr, fast = head, head, head
    prev = None

    while fast != None:
        if fast.next == None:
            break
        slow = slow.next
        fast = fast.next.next

    fast = slow.next
    slow.next = None

    # reverse second half
    while fast != None:
        hold = fast.next
        fast.next = prev
        prev = fast
        fast = hold

    while prev != None:
        hold = curr.next
        curr.next = prev
        prev = prev.next
        curr.next.next = hold
        curr = curr.next.next
