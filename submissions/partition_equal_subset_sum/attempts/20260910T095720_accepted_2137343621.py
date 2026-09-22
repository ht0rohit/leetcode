class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        subsum = sum(nums)
        if subsum % 2 != 0:
            return False
        eqsum = subsum // 2

        dp = [[-1] * (eqsum + 1) for _ in range(n + 1)]

        def backt(i, cursum):
            if cursum == eqsum:
                return True
            
            if i == n or cursum > eqsum:
                return False

            if dp[i][cursum] != -1:
                return dp[i][cursum]

            dp[i][cursum] = backt(i + 1, cursum + nums[i]) or backt(i + 1, cursum)
            return dp[i][cursum]


        return backt(0, 0)