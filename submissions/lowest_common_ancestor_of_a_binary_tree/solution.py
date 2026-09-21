# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def preorder(root):
            nonlocal lca

            if root == None:
                return False

            l = preorder(root.left)
            r = preorder(root.right)

            if (l and r) or ((root.val == p.val or root.val == q.val) and (l or r)):
                lca = root
                return True
            elif (root.val == p.val or root.val == q.val) or (l or r):
                return True
            else:
                return False


        lca = None
        preorder(root)

        return lca