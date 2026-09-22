class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[-1] * k for _ in range(n)]

        def rec(i, color):
            if dp[i][color] != -1:
                return dp[i][color]

            color1 = 2 - color if 2 - color != 1 else 0
            color2 = 3 - color if 3 - color <= 2 else 1
            
            l, r = 0, 0
            minSubCost = 0
            if i + 1 < n:
                minSubCost = float('inf')
                for c in colors:
                    if c != color:
                        minSubCost = min(minSubCost, rec(i + 1, c))

            dp[i][color] = costs[i][color] + minSubCost
            return dp[i][color]

        minCost = float('inf')
        colors = list(range(k))
        for color in colors:
            res = rec(0, color)
            minCost = min(minCost, res)

        return minCost