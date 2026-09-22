# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def treesum(root):
            if not root:
                return 0

            return root.val + treesum(root.left) + treesum(root.right)

        def postorder(root):
            nonlocal maxProd, totalSum

            if root == None:
                return 0

            leftSum = postorder(root.left)
            rightSum = postorder(root.right)

            subSum = leftSum + rightSum + root.val
            prod = (totalSum - subSum) * subSum
            maxProd = max(maxProd, prod)
            
            return subSum

        maxProd = 1
        totalSum = treesum(root)
        subSum = postorder(root)
        return maxProd