class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        res = nums[k-1] - nums[0] 
        for i in range(1, n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < res:
                res = diff

        return res
            