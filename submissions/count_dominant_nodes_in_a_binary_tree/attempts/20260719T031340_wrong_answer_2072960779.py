# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0
        maxval = float('-inf')
        
        def postorder(root, maxval):
            nonlocal count
            
            if root == None:
                return 0

            maxval = postorder(root.left, maxval)
            maxval = postorder(root.right, maxval)

            maxval = max(maxval, root.val)
            if root.val >= maxval:
                count += 1

            return maxval

        maxval = postorder(root, maxval)
        return count