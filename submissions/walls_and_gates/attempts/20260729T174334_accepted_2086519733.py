class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        q = collections.deque()


        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    rooms[nr][nc] == math.pow(2, 31) - 1
                ):
                    rooms[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))

        return rooms
