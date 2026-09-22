class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        l = len(row)

        edges = []
        for i in range(1, l, 2):
            edges.append([row[i-1] // 2, row[i] // 2])

        parent = list(range(l // 2))
        rank = [0] * (l // 2)
        res = 0
        
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

            res += 1

        for elem in edges:
            union(elem[0], elem[1])

        return res