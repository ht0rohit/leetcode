class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        # LIS DP but time complexity can go up to O(n2*m) and space complexity O(n)

        m, n = len(grid), len(grid[0])
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                cons = True
                for k in range(m):
                    if abs(grid[k][i] - grid[k][j]) > limit:
                        cons = False
                        break
                if cons:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)