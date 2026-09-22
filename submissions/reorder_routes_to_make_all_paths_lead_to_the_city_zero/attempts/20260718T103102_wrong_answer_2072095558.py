class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for elem in connections:
            u, v = elem[0], elem[1]
            adj[u].append(v)

        visited = set()
        count = 0
        
        def dfs(u, loccount):
            visited.add(u)

            if 0 in adj[u]:
                loccount += len(adj[u]) - 1
            
            for elem in adj[u]:
                if elem not in visited:
                    if 0 not in adj[u]:
                        loccount += 1
                    loccount = dfs(elem, loccount)
                     
            return loccount

        for i in range(n):
            loccount = 0
            if i not in visited:
                loccount = dfs(i, loccount)
                print(i, loccount)
                count += loccount

        return count