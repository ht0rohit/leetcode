class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], max(nums[0], nums[1])] + [0] * (n - 2)

        for i in range(2, n):
            if n == 3 and i == 2:
                dp[i] = max(dp[i - 1], nums[i])
            elif i != n - 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            else:
                if n % 2 == 0:
                    dp[i] = dp[i - 2] + nums[i]
                else:
                    dp[i] = dp[i - 1]
        
        return max(dp)