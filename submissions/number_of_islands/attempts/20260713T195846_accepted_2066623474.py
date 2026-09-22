class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = []

        grid_copy = [[0 for _ in range(n)] for _ in range(m)]
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid_copy[i][j] = c
                    c += 1

        adjl = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    adj.append([])
                    if i - 1 >= 0 and grid[i-1][j] == '1':
                        adj[adjl].append(grid_copy[i-1][j])
                    if j - 1 >= 0 and grid[i][j-1] == '1':
                        adj[adjl].append(grid_copy[i][j-1])
                    if j + 1 < n and grid[i][j+1] == '1':
                        adj[adjl].append(grid_copy[i][j+1])
                    if i + 1 < m and grid[i+1][j] == '1':
                        adj[adjl].append(grid_copy[i+1][j])
                    
                    adjl += 1

        visited = set()
        q = collections.deque()
        count = 0

        for i in range(adjl):
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

                if len(visited) == adjl:
                    break

        return count