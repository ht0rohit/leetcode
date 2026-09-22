# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if root == None:
                return

            l = dfs(root.left)
            r = dfs(root.right)
            if l:
                root.right = l
                while l.right:
                    l = l.right
                l.right = r
                root.left = None

            return root

        dfs(root)
    
        return root