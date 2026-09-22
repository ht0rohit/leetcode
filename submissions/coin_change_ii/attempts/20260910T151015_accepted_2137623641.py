class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i][j - coins[i]] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        
        return dp[0][amount]