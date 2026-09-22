class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        subsum = sum(nums)
        if subsum % 2 != 0:
            return False
        eqsum = subsum // 2

        dp = [[False] * (eqsum + 1) for _ in range(n + 1)]
        # cursum == eqsum → True
        for i in range(n + 1):
            dp[i][eqsum] = True

        for i in range(n - 1, -1, -1):
            for s in range(eqsum + 1):
                if s + nums[i] <= eqsum:
                    dp[i][s] = dp[i + 1][s + nums[i]] or dp[i + 1][s]
                else:
                    dp[i][s] = dp[i + 1][s]

        return dp[0][0]