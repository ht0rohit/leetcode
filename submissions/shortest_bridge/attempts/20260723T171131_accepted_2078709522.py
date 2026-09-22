class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        visited = set()
        q = collections.deque()

        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    q.append((i, j))

                    while q:
                        r, c = q.popleft()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < m and
                                0 <= nc < n and
                                grid[nr][nc] == 1 and
                                (nr, nc) not in visited):
                                visited.add((nr, nc))
                                q.append((nr, nc))

                    found = True
                    break

        for i, j in visited:
            q.append((i, j, 0))

        while q:
            r, c, d = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited):
                    if grid[nr][nc] == 1:
                        return d
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
