"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        def inorder(root):
            if root == None:
                return None, None

            l_head, l_tail = inorder(root.left)
            r_head, r_tail = inorder(root.right)
            
            if l_tail:
                l_tail.right = root
                root.left = l_tail
            if r_head:
                r_head.left = root
                root.right = r_head

            return l_head or root, r_tail or root

        head, tail = inorder(root)

        head.left = tail
        tail.right = head
        
        return head