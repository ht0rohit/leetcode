class Solution:
    def stoneGame(self, piles):
        n = len(piles)

        dp = [[0] * n for _ in range(n)]

        # One pile: current player takes it
        for i in range(n):
            dp[i][i] = piles[i]

        # Fill upper triangle
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                dp[l][r] = max(
                    piles[l] - dp[l + 1][r],
                    piles[r] - dp[l][r - 1]
                )

        return dp[0][n - 1] > 0