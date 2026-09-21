class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        i, j, k = 0, 1, 2
        minsum = 151

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        minsum = min(minsum, nums[i] + nums[j] + nums[k])

        return -1 if minsum == 151 else minsum