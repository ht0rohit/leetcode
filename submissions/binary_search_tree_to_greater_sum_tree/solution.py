# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inorder(root, curSum):
            if root == None:
                return curSum

            r = inorder(root.right, curSum)
            curSum = r + root.val
            root.val = curSum
            l = inorder(root.left, curSum)

            return l

        curSum = 0
        curSum = inorder(root, curSum)
        return root