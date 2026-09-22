class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return

            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[y] < rank[x]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1

        for elem in edges:
            union(elem[0], elem[1])

        vertices = {}
        for i in range(n):
            f = find(i)
            vertices[f] = vertices.get(f, 0) + 1

        edgeC = {}
        for elem in edges:
            f = find(elem[0])
            edgeC[f] = edgeC.get(f, 0) + 1

        res = 0
        for comp, v in vertices.items():
            expected = (v * (v - 1)) // 2
            if edgeC.get(comp, 0) == expected:
                res += 1

        return res
        