class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = dp = [[101 for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            dp[0][j] = matrix[0][j]    

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])
                elif j == n - 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
                dp[i][j] += matrix[i][j]
                
        return min(dp[-1])