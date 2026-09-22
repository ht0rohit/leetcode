class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        maxsum = minsum = res = nums[0]
        curmax = curmin = 0

        for num in nums:
            curmax = max(curmax + num, num)
            maxsum = max(maxsum, curmax)

            curmin = min(curmin + num, num)
            minsum = min(minsum, curmin)

        if maxsum < 0:
            return maxsum


        return max(maxsum, total - minsum)