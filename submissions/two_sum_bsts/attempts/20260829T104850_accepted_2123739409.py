# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def binarySearch(root, target):
            while root:
                if root.val == target:
                    return True
                elif root.val > target:
                    root = root.left
                else:
                    root = root.right

            return False

        def dfs(root):
            if not root:
                return False

            if binarySearch(root2, target - root.val):
                return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root1)