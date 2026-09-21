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
                return None, None

            l_head, l_tail = dfs(root.left)
            r_head, r_tail = dfs(root.right)
            if l_head:
                l_tail.right = r_head
                root.right = l_head
                root.left = None

            return root, r_tail or l_tail or root

        dfs(root)
    
        return root