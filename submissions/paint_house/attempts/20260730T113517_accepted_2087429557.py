class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[-1] * 3 for _ in range(n)]

        def rec(i, color):
            if dp[i][color] != -1:
                return dp[i][color]

            color1 = 2 - color if 2 - color != 1 else 0
            color2 = 3 - color if 3 - color <= 2 else 1
            
            l, r = 0, 0
            if i + 1 < n:
                l = rec(i + 1, color1)
                r = rec(i + 1, color2)

            dp[i][color] = costs[i][color] + min(l, r)
            return dp[i][color]

        minCost = float('inf')
        colors = [0, 1, 2]
        for color in colors:
            res = rec(0, color)
            minCost = min(minCost, res)

        return minCost