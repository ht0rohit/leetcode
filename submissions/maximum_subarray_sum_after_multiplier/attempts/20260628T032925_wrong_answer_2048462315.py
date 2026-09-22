class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        import math
        l = len(nums)
        if l == 1:
            if nums[0] >= 0:
                return nums[0] * k
            else:
                return math.ceil(nums[0] / k)

        i, j = 0, 0
        max_i, max_j = 0, 0
        maxSum, curSum = nums[0], 0
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

        if maxSum >= 0:
            for x in range(max_i, max_j + 1):
                nums[x] *= k
        else:
            for x in range(max_i, max_j + 1):
                if nums[x] >= 0:
                    nums[x] //= k
                else:
                    nums[x] = math.ceil(nums[x] / k)

        i = 0
        opSum, curSum = nums[0], 0
        while i < l:
            curSum += nums[i]
            opSum = max(opSum, curSum)
            if curSum < 0:
                curSum = 0
            i += 1
        
        return int(opSum)