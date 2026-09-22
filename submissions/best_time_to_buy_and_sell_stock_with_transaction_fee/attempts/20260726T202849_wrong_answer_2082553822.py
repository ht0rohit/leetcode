class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 1:
            return 0

        dp = [0] * (n + 1)
        minimum = 0
        i, j = 0, 1
        
        while j < n:
            if prices[j] <= prices[j - 1]:
                minimum = min(minimum, prices[j])
                dp[j] = max(prices[j] - prices[minimum] - fee + dp[minimum - 1], dp[j - 1])
                i = j
            else:
                dp[j] = max(prices[j] - prices[minimum] - fee + dp[minimum - 1], prices[j] - prices[i] - fee + dp[i - 1])
            j += 1

            print(dp)

        return dp[-2]