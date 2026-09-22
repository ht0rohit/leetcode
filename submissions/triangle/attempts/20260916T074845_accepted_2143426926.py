class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n, m = len(triangle), len(triangle[-1])
        dp = [float('inf')] * m
        dp[0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i, -1, -1):
                if i == j:
                    dp[j] = dp[j-1]   
                elif j != 0:
                    dp[j] = min(dp[j], dp[j-1])
                
                dp[j] += triangle[i][j]


        return min(dp)