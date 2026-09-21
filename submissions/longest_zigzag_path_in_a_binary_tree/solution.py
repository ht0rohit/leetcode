# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curlen, flag):
            nonlocal maxlen

            if root == None:
                maxlen = max(maxlen, curlen)
                return

            if flag == 0:
                dfs(root.left, curlen + 1, 1)
                dfs(root.right, 0, 0)
            else:
                dfs(root.left, 0, 1)
                dfs(root.right, curlen + 1, 0)

        maxlen = 0
        dfs(root, -1, 0)

        return maxlen