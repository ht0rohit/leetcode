class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        hmap = {elem: True for elem in days}
        valid_pass = [1, 7, 30]

        num_days = days[-1]
        max_cost = int(((365 / 30) * costs[2]) + 1)
        dp = [0] + [max_cost] * num_days

        for i in range(1, num_days + 1):
            for j in range(len(valid_pass)):
                if i in hmap:
                    if i - valid_pass[j] >= 0:
                        dp[i] = min(dp[i], dp[i - valid_pass[j]] + costs[j])
                else:
                    dp[i] = dp[i - 1]

        return dp[-1]