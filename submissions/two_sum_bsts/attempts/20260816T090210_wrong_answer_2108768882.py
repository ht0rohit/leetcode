# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def dfs(root1, root2):
            if root1 == None or root2 == None:
                return False

            l = dfs(root1.left, root2.right)
            if l:
                return l
            
            cursum = root1.val + root2.val
            if cursum == target:
                return True
            elif cursum > target:
                return dfs(root1, root2.left)
            else:
                return dfs(root1.right, root2)
            

        res = dfs(root1, root2)

        return res