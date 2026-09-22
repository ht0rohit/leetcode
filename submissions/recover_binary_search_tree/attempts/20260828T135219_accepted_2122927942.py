class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        
        def inorder(root):
            nonlocal first, second, prev

            if root is None:
                return

            inorder(root.left)
            
            if prev and root.val < prev.val:
                second = root
                # The first swap occurence
                if first is None:
                    first = prev
                # The second swap occurence
                else:
                    return
            prev = root
            
            inorder(root.right)

        first = second = prev = None
        inorder(root)
        first.val, second.val = second.val, first.val