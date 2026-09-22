class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n, m = len(costs), len(costs[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        def rec(i, color):
            if i == n:
                return 0
            if dp[i][color]:
                return dp[i][color]

            color1 = 2 - color
            color2 = 3 - color if 3 - color <= 2 else 1
            
            l, r = 0, 0
            if i + 1 < n:
                l = rec(i + 1, color1)
                dp[i+1][color1] = l
                r = rec(i + 1, color2)
                dp[i+1][color2] = r

            return costs[i][color] + min(l, r)


        minCost = float('inf')
        colors = [0, 1, 2]
        for color in colors:
            res = rec(0, color)
            minCost = min(minCost, res)

        return minCost