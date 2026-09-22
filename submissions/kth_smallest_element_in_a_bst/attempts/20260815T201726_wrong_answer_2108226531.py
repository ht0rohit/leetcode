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
            
            if root == None:
                return
                
            dfs(root.left)
            if count == k:
                return root.val
            count += 1
            dfs(root.right)
            
            
        count = 1
        dfs(root)
        
        return count