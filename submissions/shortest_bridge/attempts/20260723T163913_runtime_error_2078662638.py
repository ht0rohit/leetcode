class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        visited = set()
        q = collections.deque()
        island = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island.append({(i, j)})
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
                                island[-1].add((nr, nc))
                                q.append((nr, nc))

        small = min(len(island[0]), len(island[1]))
        large = 0 if small else 1
        visited = set()
        q = collections.deque()

        for elem in island[small]:
            i, j = elem[0], elem[1]
            if (i, j) not in visited:
                visited.add((elem[0], elem[1]))
                q.append((elem[0], elem[1], 0))

                while q:
                    r, c, d = q.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (0 <= nr < m and
                            0 <= nc < n and
                            (nr, nc) not in visited):
                            visited.add((nr, nc))
                            q.append((nr, nc, d + 1))
                            if (nr, nc) in island[large]:
                                return d

