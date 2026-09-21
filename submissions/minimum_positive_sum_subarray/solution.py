class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = float('inf')
        
        for elem in range(l, r+1):
            i, j = 0, elem - 1
            curSum = sum(nums[i:j+1])
            while j < n:
                res = curSum if curSum > 0 and curSum < res else res
                i += 1
                j += 1
                if j < n:
                    curSum = curSum - nums[i-1] + nums[j]

        return res if res != float('inf') else -1
