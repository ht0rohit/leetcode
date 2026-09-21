# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0

        def postorder(node):
            nonlocal count

            if not node:
                return float('-inf')

            left_max = postorder(node.left)
            right_max = postorder(node.right)

            subtree_max = max(node.val, left_max, right_max)
            if node.val == subtree_max:
                count += 1

            return subtree_max

        postorder(root)
        return count