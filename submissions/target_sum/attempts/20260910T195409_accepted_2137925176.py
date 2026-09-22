class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = sum(nums)
        dp = [[None] * (2 * offset + 1) for _ in range(n + 1)]


        def rec(i, cursum):
            
            if i == n:
                return 1 if cursum == target else 0
            
            idx = cursum + offset
            if dp[i][idx] != None:
                return dp[i][idx]

            dp[i][idx] = rec(i + 1, cursum + nums[i]) + rec(i + 1, cursum - nums[i])
            
            return dp[i][idx]


        return rec(0, 0)