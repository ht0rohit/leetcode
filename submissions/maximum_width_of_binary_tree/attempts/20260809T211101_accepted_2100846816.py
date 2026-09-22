# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(root, 1)])

        maxwidth = 0
        while q:
            
            n = len(q)
            firstNode = q[0][1]
                
            for _ in range(n):
                node, w = q.popleft()
                
                if node.left != None:
                    x = 2 * w - 1
                    q.append((node.left, x))
                if node.right != None:
                    x = 2 * w
                    q.append((node.right, x))
                    
            maxwidth = max(maxwidth, w - firstNode + 1)

        return maxwidth