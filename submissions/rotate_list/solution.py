# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, curr, lennode = head, head, head

        count = 0
        while lennode:
            count += 1
            lennode = lennode.next

        for i in range(k % count):
            curr = curr.next

        while curr and curr.next:
            curr = curr.next
            prev = prev.next
        
        curr.next = head
        temp = prev
        prev = prev.next
        temp.next = None

        return prev