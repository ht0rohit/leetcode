class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l == 0:
            return 0 if target <= nums[0] else 1

        i, j = 0, l
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        
        return j