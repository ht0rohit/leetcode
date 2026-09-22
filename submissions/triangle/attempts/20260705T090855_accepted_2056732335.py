class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(i + 1):
                if j == i:
                    dp[i][j] = dp[i-1][j-1]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])
                elif i > 0:
                    dp[i][j] = dp[i-1][j]

                dp[i][j] += triangle[i][j]

        return min(dp[-1])