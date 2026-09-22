class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    q = collections.deque()
                    q.append((i, j))
                    grid[i][j] = 1

                    while q:
                        r, c = q.popleft()

                        if r - 1 > 0 and grid[r-1][c] == 0:
                            grid[r-1][c] = 1
                            q.append((r-1, c))
                        elif r - 1 == 0 and grid[r-1][c] == 0:
                            break
                        if c - 1 > 0 and grid[r][c-1] == 0:
                            grid[r][c-1] = 1
                            q.append((r, c-1))
                        elif c - 1 == 0 and grid[r][c-1] == 0:
                            break
                        if c + 1 < n - 1 and grid[r][c+1] == 0:
                            grid[r][c+1] = 1
                            q.append((r, c+1))
                        elif c + 1 == n - 1 and grid[r][c+1] == 0:
                            break
                        if r + 1 < m - 1 and grid[r+1][c] == 0:
                            grid[r+1][c] = 1
                            q.append((r+1, c))
                        elif r + 1 == m - 1 and grid[r+1][c] == 0:
                            break
                    else:
                        count += 1

        return count