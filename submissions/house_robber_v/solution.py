class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        l = len(nums)
        
        dp = [0, 0, 0] + [0 for i in range(l)]
        dp[3] = nums[0]
        
        for i in range(1, l):
            if colors[i-1] == colors[i]:
                dp[i+3] = max(dp[i], dp[i+1])
            else:
                dp[i+3] = max(dp[i], dp[i+1], dp[i+2])

            dp[i+3] += nums[i]

        print(dp)
        return max(dp)