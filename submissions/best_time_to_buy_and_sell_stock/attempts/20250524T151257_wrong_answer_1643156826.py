class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_sell_last = 0
        max_profit_buy_index = len(prices) - 1
        for i in range(len(prices)):
            profit = prices[-1] - prices[i]
            if profit > max_profit_sell_last:
                max_profit_buy_index = i
                max_profit_sell_last = profit

        rolling_profit = max_profit_sell_last
        max_profit = max_profit_sell_last
        for i in range(len(prices)-2, max_profit_buy_index-1, -1):
            rolling_profit = rolling_profit + (prices[i] - prices[i+1])
            if rolling_profit > max_profit:
                max_profit = rolling_profit

        return max_profit