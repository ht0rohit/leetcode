# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inOrder(root):
            nonlocal lastNode

            if root is None:
                return True

            l = inOrder(root.left)

            if not l or (lastNode and root.val < lastNode):
                return False
            lastNode = root.val
            
            r = inOrder(root.right)

            return r if r else False

        lastNode = None
        return inOrder(root)