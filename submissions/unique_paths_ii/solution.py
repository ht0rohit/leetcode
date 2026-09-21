class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0

        i = 1
        while i < m:
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
                i += 1
            else:
                while i < m:
                    dp[i][0] = 0
                    i += 1

        j = 1
        while j < n:
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
                j += 1
            else:
                while j < n:
                    dp[0][j] = 0
                    j += 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[m-1][n-1]