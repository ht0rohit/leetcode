class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        i, j, it = 0, 0, 1
        cursum = 0
        res = nums[0]

        while it < 2 * n:
            cursum += nums[j % n]
            res = max(res, cursum)
            if cursum < 0:
                cursum = 0
                i = j + 1

            j += 1
            if i != j and i % n == j % n:
                cursum = 0
                i += 1
                while i < n and nums[i] < 0:
                    i += 1
                j = i

            it += 1



        return res