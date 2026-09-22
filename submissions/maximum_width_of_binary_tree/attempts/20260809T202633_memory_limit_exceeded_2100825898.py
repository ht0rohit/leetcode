# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])

        maxwidth = 1
        while q:
            
            n = len(q)
            i, j = 0, n - 1
            while q and q[0] == None and i < n:
                q.popleft()
                i += 1
            while q and q[-1] == None and j >= 0:
                q.pop()
                j -= 1
                
            maxwidth = max(maxwidth, j - i + 1)
            
            print(i, j, n, maxwidth)
                
            for k in range(i, j + 1):
                node = q.popleft()

                if node == None:
                    q.append(None)
                    q.append(None)
                    continue
                
                if node.left != None:
                    q.append(node.left)
                else:
                    q.append(None)
                if node.right != None:
                    q.append(node.right)
                else:
                    q.append(None)
                

        return maxwidth