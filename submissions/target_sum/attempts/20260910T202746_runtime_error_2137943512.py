class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = sum(nums)

        dp = [0] * (2 * offset + 1)
        # Base case: no numbers left
        dp[target + offset] = 1

        
        for i in range(n - 1, -1, -1):
            next_dp = [0] * (2 * offset + 1)
            
            for cursum in range(-offset, offset + 1):
                idx = cursum + offset

                if cursum + nums[i] <= offset:
                    next_dp[idx] += dp[idx + nums[i]]

                if cursum - nums[i] >= -offset:
                    next_dp[idx] += dp[idx - nums[i]]

            dp = next_dp
        

        return dp[offset]