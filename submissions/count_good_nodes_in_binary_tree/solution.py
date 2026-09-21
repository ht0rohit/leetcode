# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = root.val
        count = 0

        def good(root, maxx):
            nonlocal count

            if root == None:
                return

            if maxx <= root.val:
                count += 1
                maxx = root.val
            good(root.left, maxx)
            good(root.right, maxx)

        good(root, maxx)
        return count