# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hmap = {}
        curr = head
        
        i = 0
        while curr:
            if curr.val in hmap:
                return True
            hmap[i] = curr.val
            curr = curr.next
            i += 1