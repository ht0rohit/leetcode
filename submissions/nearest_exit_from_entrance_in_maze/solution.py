class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                is_border = i == 0 or i == m - 1 or j == 0 or j == n - 1
                if is_border and maze[i][j] == '.' and [i, j] != entrance:
                    maze[i][j] = '+'
                    q.append((i, j, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if [nr, nc] == entrance:
                    return steps + 1

                if maze[nr][nc] == '.':
                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps + 1))

        return -1