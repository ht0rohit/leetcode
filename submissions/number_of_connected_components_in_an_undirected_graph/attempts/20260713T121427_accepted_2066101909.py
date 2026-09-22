class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for elem in edges:
            adj[elem[0]].append(elem[1])
            adj[elem[1]].append(elem[0])

        visited = set()
        q = collections.deque([0])
        count = 0

        for i in range(n):

            if i not in visited:
                count += 1
                visited.add(i)
                q.append(i)

                while q:
                    u = q.popleft()

                    for j in range(len(adj[u])):
                        if adj[u][j] not in visited:
                            visited.add(adj[u][j])
                            q.append(adj[u][j])

                if len(visited) == n:
                    break

        return count