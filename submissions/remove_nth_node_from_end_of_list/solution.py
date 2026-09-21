# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        temp = ListNode()
        left = temp
        left.next = head
        right = head

        for i in range(n - 1):
            right = right.next

        while right and right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return temp.next