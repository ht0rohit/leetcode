# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = root.val
        
        def path(root):
            nonlocal maxsum

            if not root:
                return 0
            
            l = path(root.left)
            r = path(root.right)
            cursum = l + r + root.val
            maxsum = max(maxsum, cursum)

            res = max(l, r) + root.val
            return res if res > 0 else 0

        path(root)
        return maxsum
