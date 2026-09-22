class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0] * (n+1)
        res[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            res[i] = res[i+1] + nums[i]

        cursum = 0
        for i in range(n):
            res[i] = abs((nums[i] * i) - cursum) + abs((nums[i] * (n-i-1)) - res[i+1])
            cursum += nums[i]

        return res[:-1]