# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        def find_depth(root):
            if root == None:
                return 0

            count = 1 + find_depth(root.left)
            return count

        depth = find_depth(root)

        def dfs(root, d, w):
            nonlocal maxw, flag

            if root == None:
                return None

            if root.right == None and root.left == None and d == depth and flag:
                flag = 0
                maxw += w

            if not flag:
                return None

            dfs(root.right, d + 1, w*2)
            dfs(root.left, d + 1, w*2 - 1)
            

        maxw = 2 ** (depth - 1) - 1
        flag = 1
        dfs(root, 1, 1)

        return maxw