class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        l = len(row)

        edges = []
        for i in range(1, l, 2):
            edges.append([row[i-1] // 2, row[i] // 2])

        adj = [[] for _ in range(l // 2)] 
        for elem in edges:
            adj[elem[0]].append(elem[1])
            adj[elem[1]].append(elem[0])
        adj = [list(set(elem)) for elem in adj]

        visited = set()
        q = collections.deque()

        count = 0
        for i in range(len(adj)):
            if i not in visited:
                visited.add(i)
                q.append(i)
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if v not in visited:
                            count += 1
                            visited.add(v)
                            q.append(v)

                if len(visited) == len(adj):
                    break

        return count