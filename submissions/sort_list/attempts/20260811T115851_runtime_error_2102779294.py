# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            node = ListNode()
            merged = node

            l1, l2 = left, right

            while l1 and l2:
                if l1.val <= l2.val:
                    merged.next = l1
                    l1 = l1.next
                else:
                    merged.next = l2
                    l2 = l2.next

                merged = merged.next
            
            merged.next = l1 if l1 else l2

            return node.next

        
        def merge_sort(curr, n):
            if curr.next == None:
                return curr

            mid = n // 2

            c = curr
            it = 1
            while it < mid - 1:
                it -= 1
                c = c.next

            r = c.next
            c.next = None

            left = merge_sort(curr, n - mid)
            right = merge_sort(r, n - mid + 1)

            return merge(left, right)

        if head == None:
            return head

        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        curr = head
        res = merge_sort(curr, n)

        return res