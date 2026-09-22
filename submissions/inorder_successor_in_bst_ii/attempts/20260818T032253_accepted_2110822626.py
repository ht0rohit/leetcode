"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        value = node.val
        res = None
        
        if not node.right:
            while node.parent:
                if node.parent.val > value:
                    return node.parent
                node = node.parent
            return None

        while node:
            if node.val > value:
                res = node
                node = node.left
            else:
                node = node.right

        return res