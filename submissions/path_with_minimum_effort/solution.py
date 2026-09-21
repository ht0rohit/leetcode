class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        path = [[float('inf') for _ in range(n)] for _ in range(m)]
        path[0][0] = 0
        q = [(0, 0, 0)]

        while q:
            effort, i, j = heapq.heappop(q)
            
            if effort > path[i][j]:
                continue

            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < m and 0 <= c < n:

                    update = max(effort, abs(heights[r][c] - heights[i][j]))
                    if update < path[r][c]:
                        path[r][c] = update
                        heapq.heappush(q, (path[r][c], r, c))


        return path[-1][-1]