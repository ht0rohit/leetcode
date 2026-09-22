# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        head = ListNode()
        merged = head

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                merged.next = curr1
                merged = merged.next
                curr1 = curr1.next
            else:
                merged.next = curr2
                merged = merged.next
                curr2 = curr2.next

        if curr1:
            while curr1:
                merged.next = curr1
                merged = merged.next
                curr1 = curr1.next

        elif curr2:
            while curr2:
                merged.next = curr2
                merged = merged.next
                curr2 = curr2.next

        return head.next
