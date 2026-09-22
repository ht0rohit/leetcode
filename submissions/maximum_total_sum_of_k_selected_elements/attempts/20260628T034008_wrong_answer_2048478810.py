class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        maxSum = 0
        for i in range(k):
            if mul:
                maxSum = maxSum + (nums[i] * mul)
                mul -= 1
            else:
                maxSum += nums[i]
                mul -= 1

        return maxSum