class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        time = grid[0][0]
        swim = [[n*n for _ in range(n)] for _ in range(n)]
        swim[0][0] = time
        q = [(time, 0, 0)]

        while q:
            time, i, j = heapq.heappop(q)
            
            if time > swim[i][j]:
                continue

            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < n and 0 <= c < n:

                    update = time + max(grid[r][c] - time, 0)
                    if update < swim[r][c]:
                        swim[r][c] = update
                        heapq.heappush(q, (swim[r][c], r, c))


        return swim[-1][-1]