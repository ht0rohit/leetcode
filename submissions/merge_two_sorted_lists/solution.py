# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        merged = head

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                merged.next = curr1
                curr1 = curr1.next
            else:
                merged.next = curr2
                curr2 = curr2.next
            merged = merged.next

        merged.next = curr1 if curr1 else curr2

        return head.next
