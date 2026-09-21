# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return

        l = self.removeLeafNodes(root.left, target)
        r = self.removeLeafNodes(root.right, target)

        if not l:
            root.left = None
        if not r:
            root.right = None

        if l == None and r == None and root.val == target:
            root = None

        return root
