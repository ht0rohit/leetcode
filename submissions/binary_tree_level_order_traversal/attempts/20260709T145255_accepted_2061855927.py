# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root, None])

        res = [[]]
        while q:
            node = q.popleft()
            if node == None:
                if q:
                    q.append(None)
                    res.append([])
                    continue
                else:
                    break
            else:
                res[-1].append(node.val)
            
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

        return res