class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = collections.deque()
        q.append([])
        
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q[0].append((i, j))
                if grid[i][j] == 1:
                    flag = True

        if not q[0] and not flag:
            return 0

        elapsed = -1
        while q[0]:
            q.append([])
            elapsed += 1

            for elem in q[0]:
                r, c = elem[0], elem[1]

                if r - 1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q[-1].append((r-1, c))
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q[-1].append((r, c-1))
                if c + 1 < n and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q[-1].append((r, c+1))
                if r + 1 < m and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q[-1].append((r+1, c))

            q.popleft()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
            
        return elapsed