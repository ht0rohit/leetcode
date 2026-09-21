class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i, j = 0, 1
        while j < l:
            if nums[i] == 0:
                while j + 1 < l and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

        return nums
        