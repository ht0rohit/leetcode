# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root):
            nonlocal count
            
            if not root:
                return None
            
            # Left
            res = dfs(root.left)
            if res is not None:
                return res
            
            # Current
            count += 1
            if count == k:
                return root.val
            
            # Right
            return dfs(root.right)
        
        count = 0
        return dfs(root)