# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(l, r):
            if l > r:
                return

            mid = l + (r - l) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node


        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = dfs(0, mid - 1)
        root.right = dfs(mid + 1, n - 1)

        return root