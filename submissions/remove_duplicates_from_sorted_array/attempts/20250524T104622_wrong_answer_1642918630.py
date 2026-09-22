class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while i < (len(nums) - 1) and j < len(nums) and i < j:
            if nums[j] == nums[i]:
                while j < len(nums) and nums[j] == nums[i]:
                    j += 1
                if j < len(nums):
                    temp = nums[i+1]
                    nums[i+1] = nums[j]
                    nums[j] = temp
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        
        return i+1
