class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1,1] for _ in range(n)]

        for i in range(1, n):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                    elif dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]

        lis = max(dp)[0]
        count = 0
        for sub, num in dp:
            if sub == lis:
                count += num

        
        return count