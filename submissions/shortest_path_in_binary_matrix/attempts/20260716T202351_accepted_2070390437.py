class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        elif m == 1 and n == 1:
            return 1

        q = deque([(0, 0, 1)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if [nr, nc] == [m - 1, n - 1]:
                    return steps + 1

                if grid[nr][nc] == 0:
                    grid[nr][nc] = steps + 1
                    q.append((nr, nc, steps + 1))

        return -1