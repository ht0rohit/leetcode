# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        curr = root
        prev = None
        while curr:
            if curr.val == key:
                break
            prev = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        else:
            # Key not found
            return root

        templ, tempr = curr.left, curr.right
        curr.left, curr.right = None, None
        temp, temppr = None, None
        if tempr:
            temp = tempr
            while temp.left:
                temppr = temp
                temp = temp.left
        elif templ:
            temp = templ
            while temp.right:
                temppr = temp
                temp = temp.right

        if temppr is None:
            if tempr:
                temp.left = templ
            elif templ:
                temp.right = tempr
        else:
            if tempr:
                temppr.left = temp.right
            elif templ:
                temppr.right = temp.left
            temp.left = templ
            temp.right = tempr

        if prev:
            if curr.val > prev.val:
                prev.right = temp
            else:
                prev.left = temp
            return root
        else:
            return temp