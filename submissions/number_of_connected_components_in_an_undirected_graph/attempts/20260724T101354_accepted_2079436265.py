class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        seen = set()
        res = 0
        for node in range(n):
            f = find(node)
            if f not in seen:
                seen.add(f)
                res += 1

        return res
