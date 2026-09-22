class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        recSet = {}
        recStack = []

        def dfs(u, parent):
            visited.add(u)
            recSet[u] = len(recStack)
            recStack.append(u)

            for v in adj[u]:
                if v not in visited:
                    cycle = dfs(v, u)
                    if cycle:
                        return cycle
                elif v != parent and v in recSet:
                    return recStack[recSet[v]:]

            recStack.pop()
            recSet.pop(u)
            return None


        cycle = set(dfs(1, None))

        res = []
        for elem in edges:
            if elem[0] in cycle and elem[1] in cycle:
                res = elem

        return res