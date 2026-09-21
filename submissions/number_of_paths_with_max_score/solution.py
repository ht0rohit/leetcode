class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board)
        dp = [[[-1, 0] for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = [0, 1]

        for i in range(m - 2, -1, -1):
            if board[i][n-1] != 'X' and  dp[i+1][n-1][0] != -1:
                dp[i][n-1] = [int(board[i][n-1]) + dp[i+1][n-1][0], 1]
            else:
                break

        for j in range(n - 2, -1, -1):
            if board[m-1][j] != 'X' and dp[m-1][j+1][0] != -1:
                dp[m-1][j] = [int(board[m-1][j]) + dp[m-1][j+1][0], 1]
            else:
                break

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                maxsum = max(dp[i+1][j][0], dp[i][j+1][0], dp[i+1][j+1][0])
                paths = 0
                for r, c in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if dp[r][c][0] == maxsum:
                        paths += dp[r][c][1]
                if i == 0 and j == 0:
                    dp[i][j][0] = maxsum if maxsum != -1 else 0
                    dp[i][j][1] = paths
                elif board[i][j] != 'X':
                    dp[i][j][0] = int(board[i][j]) + maxsum if maxsum != -1 else maxsum
                    dp[i][j][1] = paths

        MOD = 10**9 + 7
        return [dp[0][0][0], dp[0][0][1] % MOD]