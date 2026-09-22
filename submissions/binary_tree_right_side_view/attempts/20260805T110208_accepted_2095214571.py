# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        q = collections.deque([root, None])
        
        res = []
        node = None
        while q:
            prev = node
            node = q.popleft()

            if node == None:
                res.append(prev.val)
                if q:
                    q.append(None)
                    continue
                break

            if node.left != None:
                q.append(node.left)

            if node.right != None:
                q.append(node.right)

        return res
