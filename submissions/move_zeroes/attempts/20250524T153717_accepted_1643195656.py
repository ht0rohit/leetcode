class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, ind = 0, 0
        while i < len(nums)-1:
            if nums[i] == 0:
                while i < len(nums)-1 and nums[i] == 0:
                    i += 1
                nums[ind] = nums[i]
                nums[i] = 0
            else:
                i += 1
            ind += 1
                
        