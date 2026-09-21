class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        maxarea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    q = collections.deque()
                    q.append((i, j))
                    grid[i][j] = 0

                    while q:
                        r, c = q.popleft()
                        area += 1

                        if r - 1 >= 0 and grid[r-1][c] == 1:
                            grid[r-1][c] = 0
                            q.append((r-1, c))
                        if c - 1 >= 0 and grid[r][c-1] == 1:
                            grid[r][c-1] = 0
                            q.append((r, c-1))
                        if c + 1 < n and grid[r][c+1] == 1:
                            grid[r][c+1] = 0
                            q.append((r, c+1))
                        if r + 1 < m and grid[r+1][c] == 1:
                            grid[r+1][c] = 0
                            q.append((r+1, c))

                    maxarea = max(maxarea, area)

        return maxarea