# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        root = TreeNode(preorder[0])
        st = [root]

        for i in range(1, n):
            node = TreeNode(preorder[i])

            curr = st[-1]
            while st and node.val > st[-1].val:
                curr = st.pop()

            st.append(node)
            if node.val > curr.val:
                curr.right = node
            else:
                curr.left = node

        return root