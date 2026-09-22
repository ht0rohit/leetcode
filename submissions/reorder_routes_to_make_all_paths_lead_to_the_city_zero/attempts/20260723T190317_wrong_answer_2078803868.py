class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for elem in connections:
            u, v = elem[0], elem[1]
            adj[u].append(v)
        
        visited = set()
        direction = [False] * len(adj)
        direction[0] = True
        count = 0
        
        def dfs(u):
            nonlocal count

            visited.add(u)

            for v in adj[u]:
                if direction[v] == True:
                    direction[u] = True
                elif v in visited:
                    count += 1
                    direction[v] = True
                else:
                    if direction[u] == True:
                        count += 1
                        direction[v] = True
                    dfs(v)


        for i in range(n):
            if i not in visited:
                dfs(i)

        return count