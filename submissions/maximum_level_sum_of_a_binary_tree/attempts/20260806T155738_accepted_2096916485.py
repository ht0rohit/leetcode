# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])

        maxsum = float('-inf')
        res, level = 0, 0
        while q:
            cursum = 0

            for _ in range(len(q)):
                node = q.popleft()
                cursum += node.val
                
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            
            level += 1

            if cursum > maxsum:
                maxsum = cursum    
                res = level

        return res
