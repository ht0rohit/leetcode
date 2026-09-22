class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        res = n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal res

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
            
            res -= 1

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i + 1, j + 1)

        return res
