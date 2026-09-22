# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mind = math.pow(10,5) + 1

        def minDiff(root):
            nonlocal mind

            if root == None:
                return 0
            if root.left != None:
                mind = min(mind, abs(root.val - root.left.val))
            if root.right != None:
                mind = min(mind, abs(root.val - root.right.val))    
                
            mind = min(mind, self.minDiffInBST(root.left), self.minDiffInBST(root.right))

        minDiff(root)
        return mind

