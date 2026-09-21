# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 1

        def postorder(root):
            nonlocal count

            if root == None:
                return 1

            l = postorder(root.left)
            r = postorder(root.right)

            tempcount = min(l, r) + 1
            if l > 1 or r > 1:
                count += 1
                tempcount = 0

            return tempcount

        count = 0
        res = postorder(root)
        if res > 1:
            count += 1
        return count

        