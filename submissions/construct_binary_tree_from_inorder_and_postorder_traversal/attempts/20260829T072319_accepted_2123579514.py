# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        hmap = {}
        for i in range(n):
            hmap[inorder[i]] = i

        root = TreeNode(postorder[-1])
        st = [root]

        for i in range(n - 2, -1, -1):
            node = TreeNode(postorder[i])
            nind = hmap[node.val]
            
            curr = st[-1]
            while st and nind < hmap[st[-1].val]:
                curr = st.pop()
            
            if nind < hmap[curr.val]:
                curr.left = node
            else:
                curr.right = node

            st.append(node)


        return root