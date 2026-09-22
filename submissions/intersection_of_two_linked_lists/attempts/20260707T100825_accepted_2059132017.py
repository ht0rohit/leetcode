# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        l1, l2 = 0, 0

        while currA:
            currA = currA.next
            l1 += 1
        while currB:
            currB = currB.next
            l2 += 1

        currA, currB = headA, headB
        if l1 > l2:
            for i in range(abs(l1-l2)):
                currA = currA.next
        else:
            for i in range(abs(l1-l2)):
                currB = currB.next
        
        while currA and currB:
            if currA == currB:
                return currA
            else:
                currA = currA.next
                currB = currB.next
        else:
            return None