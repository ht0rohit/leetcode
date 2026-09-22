# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next

        while curr:
            elem = math.gcd(prev.val, curr.val)
            node = ListNode(elem, curr)
            prev.next = node
            prev = curr
            curr = curr.next

        return head