# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        summ = ListNode()
        curr = summ

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            elem = val1 + val2 + carry
            carry = elem // 10
            elem = elem % 10

            curr.next = ListNode(elem)
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return summ.next