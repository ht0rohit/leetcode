# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        hmap = {}
        for i in range(n):
            hmap[inorder[i]] = i

        root = TreeNode(preorder[0])
        st = [root]

        for i in range(1, n):
            node = TreeNode(preorder[i])
            nind = hmap[node.val]
            
            curr = st[-1]
            while st and nind > hmap[st[-1].val]:
                curr = st.pop()
            
            if nind < hmap[curr.val]:
                curr.left = node
            else:
                curr.right = node

            st.append(node)


        return root