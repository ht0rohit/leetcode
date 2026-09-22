# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def palindrome(currNode, prevNode):
            if currNode.next == None:
                return prevNode, True

            prevNode, status = palindrome(currNode.next, prevNode)
            
            if status and prevNode and prevNode.val == currNode.next.val:
                return prevNode.next, True
            else:
                return None, False

        if head.next == None:
            return True

        curr = head
        prev = head
        _, res = palindrome(curr, prev)
        return res