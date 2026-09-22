class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal comp

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

            comp -= 1

        comp = n
        for elem in connections:
            union(elem[0], elem[1])

        return comp - 1