class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for elem in edges:
            adj[elem[0]].append(elem[1])

        visited = set()
        q = collections.deque()
        res = []

        for i in range(n):
            if i not in visited:
                visited.add(i)
                q.append(i)
                res.append(i)

                while q:
                    u = q.popleft()

                    for v in adj[u]:
                        if v not in visited:
                            visited.add(v)
                            q.append(v)

                if len(visited) == n:
                    return res