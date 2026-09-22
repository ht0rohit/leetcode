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
        if not node.right:
            if node.parent and node.parent.left == node:
                return node.parent
            return None

        value = node.val
        res = None

        while node:
            if node.val > value:
                res = node
                node = node.left
            else:
                node = node.right

        return res