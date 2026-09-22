"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        
        q = collections.deque([root])

        while q:
            n = len(q)

            for i in range(n):
                node = q.popleft()
                node.next = q[0] if i != n - 1 else None
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

        return root