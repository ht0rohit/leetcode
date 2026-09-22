class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return prices[0]

        profit = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[j] > prices[i]:
                profit += prices[j] - prices[i]
            i += 1
            j += 1

        return profit