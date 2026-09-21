# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def preorder(root, curSum):
            nonlocal maxSum

            if not root.left and not root.right:
                curSum += str(root.val)
                maxSum += int(curSum)
                return

            curSum += str(root.val)
            if root.left:
                preorder(root.left, curSum)
            if root.right:
                preorder(root.right, curSum)

        curSum, maxSum = '', 0
        preorder(root, curSum)
        return maxSum