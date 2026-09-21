class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[j] > prices[i]:
                profit += prices[j] - prices[i]
            i += 1
            j += 1

        return profit