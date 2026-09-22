# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(root):
            if root == None:
                res.append('null')
                return

            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def createbt():
            nonlocal i
            i += 1

            if data[i] == 'null':
                return

            node = TreeNode(data[i])
            
            l = createbt()
            r = createbt()

            node.left = l
            node.right = r

            return node
        

        i = -1
        data = data.split(',')
        return createbt()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))