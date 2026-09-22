class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        subsum = sum(nums)
        if subsum % 2 != 0:
            return False
        eqsum = subsum // 2

        dp = [False] * (eqsum + 1)
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for s in range(eqsum + 1):
                if s + nums[i] <= eqsum:
                    dp[s] = dp[s + nums[i]] or dp[s]

        return dp[0]