class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l == 0:
            return 0 if target <= nums[0] else 1

        i, j = 0, l - 1
        while i <= j:
            mid = (i + j) // 2
            if target <= nums[mid]:
                j = mid - 1
            elif target > nums[mid]:
                i = mid + 1
        
        if target <= nums[mid]:
            return mid
        else:
            return mid + 1