# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n or (n == 1 and not lists[0]):
            return None

        def merge(elem1, elem2):
            node = ListNode(0, None)
            curr = node

            while elem1 and elem2:
                if elem1.val <= elem2.val:
                    curr.next = elem1
                    elem1 = elem1.next
                else:
                    curr.next = elem2
                    elem2 = elem2.next
                curr = curr.next

            curr.next = elem1 if elem1 else elem2

            return node.next

        elem1 = lists[0]
        for i in range(1, n):
            elem2 = lists[i]
            res = merge(elem1, elem2)
            elem1 = res

        return res