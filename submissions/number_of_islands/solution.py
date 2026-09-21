class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        q = collections.deque()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    q.append((i, j))

                    while q:
                        r, c = q.popleft()

                        if r - 1 >= 0 and grid[r-1][c] == '1':
                            grid[r-1][c] = '0'
                            q.append((r-1, c))
                        if c - 1 >= 0 and grid[r][c-1] == '1':
                            grid[r][c-1] = '0'
                            q.append((r, c-1))
                        if c + 1 < n and grid[r][c+1] == '1':
                            grid[r][c+1] = '0'
                            q.append((r, c+1))
                        if r + 1 < m and grid[r+1][c] == '1':
                            grid[r+1][c] = '0'
                            q.append((r+1, c))

        return count