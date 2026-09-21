class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    q.append((i, j, 0))
                else:
                    isWater[i][j] = -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, height = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if isWater[nr][nc] == -1:
                    isWater[nr][nc] = height + 1
                    q.append((nr, nc, height + 1))

        return isWater