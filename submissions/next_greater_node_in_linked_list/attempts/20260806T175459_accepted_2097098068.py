# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        st = []

        i = 0
        while head:
            while st and st[-1][1] < head.val:
                ind, _ = st.pop()
                answer.append((ind, head.val))

            st.append((i, head.val))
            head = head.next
            i += 1

        while st:
            ind, val = st.pop()
            answer.append((ind, 0))

        res = [0] * len(answer)
        for ind, val in answer:
            res[ind] = val

        return res
