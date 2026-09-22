class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)

        res = 0
        l, r = 0, 0
        maxelem = -1
        
        for i in range(n):    
            maxelem = max(maxelem, nums[i])
            if left <= nums[i] <= right:
                r = i
                res += (r - l + 1)
            elif left <= maxelem <= right:
                res += (r - l + 1)
            else:
                l, r = i + 1, i + 1
                maxelem = -1


        return res