class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)

        res = 0
        l, r = 0, -1
        for i in range(n):
            
            if nums[i] > right:
                l, r = i + 1, -1
            elif left <= nums[i] <= right:
                r = i

            if r != -1:
                res += (r - l + 1)

        return res