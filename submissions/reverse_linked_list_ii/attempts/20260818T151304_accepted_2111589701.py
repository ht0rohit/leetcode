# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None or left == right:
            return head

        curr = head
        prev = None
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        
        l_prev, l = prev, curr
        for _ in range(left, right + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if l_prev:
            l_prev.next = prev
        l.next = curr

        return prev if l_prev is None else head