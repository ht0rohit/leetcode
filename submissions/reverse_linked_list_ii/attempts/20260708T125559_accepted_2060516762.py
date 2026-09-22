# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None or left == right:
            return head

        prev, slow = None, head

        if left > 1:
            prev = head
            slow = slow.next
            for i in range(2, left):
                slow = slow.next
                prev = prev.next

        sub, curr = None, slow
        it = right - left + 1
        count = 1
        while count <= it:
            temp = slow.next
            slow.next = sub
            sub = slow
            slow = temp
            count += 1
        
        curr.next = temp
        if prev:
            prev.next = sub
            return head

        return sub
        