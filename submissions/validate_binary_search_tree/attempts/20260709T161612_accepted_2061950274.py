# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lastNode = 0 - (math.pow(2,31) + 1)

        def inOrder(root):
            nonlocal lastNode

            if root == None:
                return True

            if not inOrder(root.left):
                return False
            if root.val <= lastNode:
                return False
            lastNode = root.val
            return inOrder(root.right)

        return inOrder(root)