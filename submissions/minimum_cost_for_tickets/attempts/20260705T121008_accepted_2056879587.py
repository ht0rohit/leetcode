class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        num_days = days[-1]
        hmap = set(days)
        valid_pass = [1, 7, 30]
        dp = [0] + [float('inf')] * num_days

        for i in range(1, num_days + 1):
            if i not in hmap:
                dp[i] = dp[i - 1]
                continue
            for j in range(len(valid_pass)):
                if i - valid_pass[j] >= 0:
                    dp[i] = min(dp[i], dp[i - valid_pass[j]] + costs[j])
                else:
                    dp[i] = min(dp[i], costs[j])

        return dp[-1]