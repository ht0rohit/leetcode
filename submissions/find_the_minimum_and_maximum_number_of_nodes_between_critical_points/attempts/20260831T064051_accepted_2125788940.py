# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [-1, -1]

        i = 1
        prev, curr = head, head.next
        start, end = None, None
        mind, maxd = float('inf'), float('-inf')

        while curr.next:
            
            if prev.val < curr.val > curr.next.val or \
                prev.val > curr.val < curr.next.val:
                if not start:
                    start = intm = i
                else:
                    end = i
                    mind = min(mind, end - intm)
                    intm = end
            prev, curr = curr, curr.next
            i += 1

        else:
            if end:
                maxd = end - start
                return [mind, maxd]
            return [-1, -1]