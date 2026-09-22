class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 1:
            return 0

        dp = [0] * n

        i, j = 0, 1
        for j in range(n):

            dp[j] = max(prices[j] - prices[i] - fee, dp[j-1] + prices[j] - prices[j-1] - fee, dp[j-1], dp[j])

            if prices[j] < prices[i]:
                i = j
        

        return dp[-1]