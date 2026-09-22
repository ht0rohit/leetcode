class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def helper(ind1, ind2, ocean):
            visited = set()
            q = collections.deque()

            for i in range(m):
                visited.add((i, ind1))
                q.append((i, ind1))
                if ocean == 'pacific':
                    pacific[i][ind1] = 1
                else:
                    atlantic[i][ind1] = 1
            for j in range(n):
                visited.add((ind2, j))
                q.append((ind2, j))
                if ocean == 'pacific':
                    pacific[ind2][j] = 1
                else:
                    atlantic[ind2][j] = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        (nr, nc) not in visited and
                        heights[r][c] <= heights[nr][nc]):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        if ocean == 'pacific':
                            pacific[nr][nc] = 1
                        else:
                            atlantic[nr][nc] = 1
        
        helper(0, 0, 'pacific')
        helper(n-1, m-1, 'atlantic')

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])

        return res