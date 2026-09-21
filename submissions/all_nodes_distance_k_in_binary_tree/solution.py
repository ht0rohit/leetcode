# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = collections.deque([root])
        adj = {}
        
        # Build undirected graph
        while q:
            u = q.popleft()

            if u.left:
                adj.setdefault(u, []).append(u.left)
                adj.setdefault(u.left, []).append(u)
                q.append(u.left)

            if u.right:
                adj.setdefault(u, []).append(u.right)
                adj.setdefault(u.right, []).append(u)
                q.append(u.right)

        # BFS from target
        q = collections.deque([(target, 0)])
        visited = {target}
        res = []

        while q:
            u, d = q.popleft()

            if d == k:
                res.append(u.val)
                continue

            for v in adj.get(u, []):
                if v not in visited:
                    visited.add(v)
                    q.append((v, d + 1))

        return res