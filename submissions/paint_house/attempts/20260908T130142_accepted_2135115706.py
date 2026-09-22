class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[-1] * 3 for _ in range(2)]
        dp[0] = costs[0][:]

        for house in range(1, n):
            for color in range(3):
                
                color1 = 2 - color if 2 - color != 1 else 0
                color2 = 3 - color if 3 - color <= 2 else 1
                dp[1][color] = min(dp[0][color1], dp[0][color2]) + costs[house][color]
            
            dp[0] = dp[1][:]

        return min(dp[0])