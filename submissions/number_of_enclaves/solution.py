class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        maxcount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 0
                    flag = False
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        flag = True
                    q = collections.deque()
                    q.append((i, j))
                    grid[i][j] = 0

                    while q:
                        r, c = q.popleft()
                        count += 1

                        if r - 1 >= 0 and grid[r-1][c] == 1:
                            grid[r-1][c] = 0
                            q.append((r-1, c))
                            if r - 1 == 0:
                                flag = True
                        if c - 1 >= 0 and grid[r][c-1] == 1:
                            grid[r][c-1] = 0
                            q.append((r, c-1))
                            if c - 1 == 0:
                                flag = True
                        if c + 1 < n and grid[r][c+1] == 1:
                            grid[r][c+1] = 0
                            q.append((r, c+1))
                            if c + 1 == n - 1:
                                flag = True
                        if r + 1 < m and grid[r+1][c] == 1:
                            grid[r+1][c] = 0
                            q.append((r+1, c))
                            if r + 1 == m - 1:
                                flag = True

                    if not flag:
                        maxcount += count

        return maxcount