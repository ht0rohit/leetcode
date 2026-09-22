class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        l = len(nums)
        middle = nums[l // 2]
        res = nums.count(middle) == 1
        return res
        