class Solution:
    def rob(self, nums):
        n = len(nums)
        memo = [-1] * n

        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
                
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(
                dp(i - 1),
                dp(i - 2) + nums[i]
            )

            return memo[i]

        return dp(n - 1)