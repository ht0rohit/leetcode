class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        def dfs(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    board[nr][nc] == 'O'
                ):
                    board[nr][nc] = 'E'
                    dfs(nr, nc)


        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m -1 or j == 0 or j == m -1) and board[i][j] == 'O':
                    board[i][j] = 'E'
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'
