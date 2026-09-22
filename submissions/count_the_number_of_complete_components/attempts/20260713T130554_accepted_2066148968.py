class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = collections.deque()
        res = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                q.append(i)
                nodes, edges = 1, 0

                while q:
                    u = q.popleft()

                    for j in range(len(adj[u])):
                        edges += 1
                        if adj[u][j] not in visited:
                            visited.add(adj[u][j])
                            q.append(adj[u][j])
                            nodes += 1

                edges //=  2
                if edges == (nodes * (nodes - 1)) // 2:
                    res += 1

                if len(visited) == n:
                    break

        return res