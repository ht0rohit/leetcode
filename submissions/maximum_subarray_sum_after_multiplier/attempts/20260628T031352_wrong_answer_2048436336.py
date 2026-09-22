class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        import math
        l = len(nums)
        maxSum, curSum = nums[0], 0
        if l == 1:
            if maxSum >= 0:
                return maxSum * k
            else:
                return math.ceil(maxSum / k)

        i, j = 0, 0
        max_i, max_j = 0, 0
        while j < l:
            curSum += nums[j]
            if curSum >= maxSum:
                maxSum = curSum
                max_i, max_j = i, j
            if curSum < 0:
                curSum = 0
                i = j + 1
            j += 1

        if k == 1:
            return maxSum

        opSum = 0
        if maxSum >= 0:
            for x in range(max_i, max_j + 1):
                nums[x] *= k
                opSum += nums[x]
        else:
            for x in range(max_i, max_j + 1):
                if nums[x] >= 0:
                    nums[x] //= k
                else:
                    nums[x] = math.ceil(nums[x] / k)
                opSum += nums[x]

        return int(opSum)