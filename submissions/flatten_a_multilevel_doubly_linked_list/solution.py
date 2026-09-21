"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        prev = None

        while curr:

            while curr.next and curr.child is None:
                curr = curr.next

            if curr.child:
                child = curr.child
                curr.child = None

                if curr.next:
                    temp_head = curr.next
                    temp_head.prev = None

                    temp_tail = temp_head
                    while temp_tail.next:
                        temp_tail = temp_tail.next

                    if prev:
                        temp_tail.next = prev
                        prev.prev = temp_tail

                    prev = temp_head

                curr.next = child
                child.prev = curr
                curr = child

            else:
                if prev:
                    curr.next = prev
                    prev.prev = curr
                break

        return head