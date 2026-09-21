class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        maxSum, curSum = nums[0], 0
        if l == 1:
            return maxSum

        i = 0
        while i < l:
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
            i += 1

        return maxSum