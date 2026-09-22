# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        prev = None

        def minDiff(root):
            nonlocal res, prev

            if root == None:
                return

            minDiff(root.left)

            if prev is not None:
                res = min(res, abs(root.val - prev))
            prev = root.val

            minDiff(root.right)

        minDiff(root)
        return res

