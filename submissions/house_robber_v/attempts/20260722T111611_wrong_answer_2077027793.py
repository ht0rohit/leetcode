class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        l = len(nums)
        
        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        
        for i in range(1, l):
            if colors[i-1] == colors[i]:
                if i > 1:
                    dp[i] = dp[i-2] + nums[i]
                else:
                    dp[i] = nums[i]
            else:
                if i > 1:
                    dp[i] = max(dp[i-1], dp[i-2]) + nums[i]
                else:
                    dp[i] = dp[i-1] + nums[i]
            
        return max(dp)