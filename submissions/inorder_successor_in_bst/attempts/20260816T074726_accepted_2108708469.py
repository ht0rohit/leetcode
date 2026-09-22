# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def inorder(root):
            if root == None:
                return

            l = inorder(root.left)
            if l != None:
                return l
            
            if root.val > p.val:
                return root

            r = inorder(root.right)

            return r

        res = inorder(root)
        
        return res