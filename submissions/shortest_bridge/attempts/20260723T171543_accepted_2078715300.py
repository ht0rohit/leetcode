class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()

        def dfs(r: int, c: int) -> None:
            if (r < 0 or r >= m or
                c < 0 or c >= n or
                grid[r][c] != 1):
                return

            grid[r][c] = 2 # Mark first island
            q.append((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Find and mark the first island
        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # Multi-source BFS to reach the second island
        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))

            distance += 1