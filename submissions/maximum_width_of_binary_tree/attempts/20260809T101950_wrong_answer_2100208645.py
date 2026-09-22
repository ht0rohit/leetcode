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
            curwidth = 0
            levelwidth = 0

            for _ in range(len(q)):
                node = q.popleft()

                if node == None:
                    curwidth += 2
                    continue
                
                if node.left != None:
                    curwidth += 1
                    levelwidth += curwidth
                    curwidth = 0
                    q.append(node.left)
                else:
                    curwidth += 1
                    q.append(None)

                if node.right != None:
                    curwidth += 1
                    levelwidth += curwidth
                    curwidth = 0
                    q.append(node.right)
                else:
                    curwidth += 1
                    q.append(None)

            maxwidth = max(maxwidth, levelwidth)

        return maxwidth