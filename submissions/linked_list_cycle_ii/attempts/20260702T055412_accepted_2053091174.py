# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hset = set()
        curr = head
        
        while curr:
            if curr in hset:
                return curr
            hset.add(curr)
            curr = curr.next

        return None