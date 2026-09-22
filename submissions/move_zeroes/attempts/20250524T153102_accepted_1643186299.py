class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                ind = i
                while ind < len(nums)-1 and nums[ind] == 0:
                    ind += 1
                nums[i] = nums[ind]
                nums[ind] = 0
            i += 1
                
        