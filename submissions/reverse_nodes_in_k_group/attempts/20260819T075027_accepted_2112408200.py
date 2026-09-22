# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        it = n // k
        node = ListNode(0, None)
        snode = node
        while it:
            curr = head
            prev = None
            group = 0

            while group < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                group += 1

            snode.next = prev
            snode = head
            head = curr
            it -= 1

        snode.next = curr
                
        return node.next