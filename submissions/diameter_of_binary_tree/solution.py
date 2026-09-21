# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = 0
        
        def diameter(root):
            nonlocal maxd

            if not root:
                return 0
            
            l = diameter(root.left)
            r = diameter(root.right)

            maxd = max(maxd, (l + 1) + (r + 1))
            return max(l + 1, r + 1)

        diameter(root)
        return maxd - 2
