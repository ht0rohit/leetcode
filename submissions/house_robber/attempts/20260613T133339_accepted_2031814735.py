class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[1], nums[0] + nums[2])

        max_sum = [nums[0], max(nums[0], nums[1]),
                    max(nums[1], nums[0] + nums[2])] + [0] * (n - 3)

        for i in range (3, n):
            max_sum[i] = max(max_sum[i-1], max_sum[i-2] + nums[i])

        return max_sum[n-1]