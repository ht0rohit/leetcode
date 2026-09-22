class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 1:
            return 0

        dp = [0] * (n + 1)
        minimum = prices[0]
        min_ind = 0
        i, j = 0, 1
        
        while j < n:
            if prices[j] < prices[min_ind]:
                minimum = prices[j]
                min_ind = j
            if prices[j] <= prices[j - 1]:
                dp[j] = max(prices[j] - prices[min_ind] - fee + dp[min_ind - 1], dp[j - 1])
                i = j
            else:
                dp[j] = max(prices[j] - prices[min_ind] - fee + dp[min_ind - 1], prices[j] - prices[i] - fee + dp[i - 1])
            j += 1

            print(dp)

        return dp[-2] if dp[-2] > 0 else 0