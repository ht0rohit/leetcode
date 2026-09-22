# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        count = 0

        def postorder(root):
            nonlocal count

            if root == None:
                return

            l = postorder(root.left)
            r = postorder(root.right)

            tempcount = 0
            if (l == 0 and r == 0) or (l == 0 and r == 1) or (l == 1 and r == 0) or (not l and r == 0) or (l == 0 and not r):
                tempcount = 1
            count += tempcount

            return tempcount

        postorder(root)
        return count

        