class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for elem in edges:
            adj[elem[0]].append(elem[1])
            adj[elem[1]].append(elem[0])

        visited = set()
        recStack = []

        def dfs(u, parent):
            nonlocal cycle

            visited.add(u)
            recStack.append(u)

            for v in adj[u]:
                if v not in visited:
                    cycle = dfs(v, u)
                    if cycle:
                        return cycle
                elif v != parent and v in recStack:
                    i = recStack.index(v)
                    return recStack[i:]

            recStack.pop()
            return None

        cycle = dfs(0, None)

        visited = set(cycle)
        q = collections.deque()
        for c in cycle:
            q.append((c, 0))

        res = [0] * n
        while q:
            u, d = q.popleft()

            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append((v, d + 1))
                    res[v] = d + 1

        return res