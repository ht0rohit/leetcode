class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        for i in range(len(units)):
            units[i].sort()

        dp = [[100000] * len(units) for _ in range(len(units))]

        for i in range(len(units)):
            for j in range(len(units)):
                if i == j:
                    dp[i][i] = min(dp[i][i], units[j][0])
                else:
                    dp[i][i] = min(dp[i][i], units[j][0])
                    dp[i][j] = units[j][1]

        sum_op = [sum(dp[i]) for i in range(len(dp))]
        sum_op_0 = sum([units[i][0] for i in range(len(units))])

        res = max(sum_op + [sum_op_0])
        return res