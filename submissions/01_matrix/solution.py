class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if mat[nr][nc] == 1:
                    mat[nr][nc] = 0
                    dp[nr][nc] = steps + 1
                    q.append((nr, nc, steps + 1))

        return dp