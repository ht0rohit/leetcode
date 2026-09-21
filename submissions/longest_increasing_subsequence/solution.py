class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        sub = [nums[0]]

        for i in range(1, n):

            j = bisect_left(sub, nums[i])
            if j == len(sub):
                sub.append(nums[i])
            else:
                sub[j] = nums[i]
            dp[i] = j + 1


        return max(dp)