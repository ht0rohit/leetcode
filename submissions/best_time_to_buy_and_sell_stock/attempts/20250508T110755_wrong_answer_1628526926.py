class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = []
        for i in range(len(prices)):
            if i <= len(prices) - 2:
                profit += [prices[i+1] - prices[i]]

        p1, p2 = -1, -1
        for elem in profit:
            if elem > 0:
                p1 = profit.index(elem)
                break
        for elem in profit[p1:]:
            if elem > 0:
                p2 = profit.index(elem)

        max_profit = 0
        if p1!=-1 and p2!=-1:
            for elem in profit[p1: p2+1]:
                max_profit += elem
                print(max_profit)
        elif p1!=-1 and p2==-1:
            max_profit = profit[p1]
        else:
            max_profit = 0

        return max_profit