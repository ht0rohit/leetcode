class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = []

        for i in range(m):
            for j in range(n):
                adj.append([])
                if grid[i][j] == '1':
                    if i - 1 >= 0 and grid[i-1][j] == '1':
                        adj[-1].append(((i - 1) * n) + j)
                    if j - 1 >= 0 and grid[i][j-1] == '1':
                        adj[-1].append((i * n) + j - 1)
                    if j + 1 < n and grid[i][j+1] == '1':
                        adj[-1].append((i * n) + j + 1)
                    if i + 1 < m and grid[i+1][j] == '1':
                        adj[-1].append(((i + 1) * n) + j)

        visited = set()
        q = collections.deque()
        count = 0

        for k in range(len(adj)):
            i, j = k // n, k % n
            if grid[i][j] == '1' and k not in visited:
                count += 1
                visited.add(k)
                q.append(k)

                while q:
                    u = q.popleft()

                    for elem in adj[u]:
                        if elem not in visited:
                            visited.add(elem)
                            q.append(elem)

                if len(visited) == m * n:
                    break

        return count