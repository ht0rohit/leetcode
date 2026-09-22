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
                return -1

            if flag == 0:
                curlen = dfs(root.left, curlen + 1, 1)

            curlen = dfs(root.right, curlen + 1, 0)
            return curlen

        
        maxlen = 0
        dfs(root, -1, 0)

        return maxlen