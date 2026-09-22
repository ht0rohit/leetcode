class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [0] * n
        count = n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count

            x = find(x)
            y = find(y)
            if x == y:
                return False

            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[y] < rank[x]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1
            
            count -= 1
            return True

        for elem in edges:
            res = union(elem[0], elem[1])
            if not res:
                return False

        if count == 1:
            return True
        return False
