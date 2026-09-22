class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max, max_cont = 0, 0
        while j < len(prices):
            if prices[j] > prices[i]:
                diff = prices[j] - prices[i]
                max_cont = diff
                if max_cont > max:
                    max = max_cont
                j += 1
            else:
                i += 1; j += 1

        return max