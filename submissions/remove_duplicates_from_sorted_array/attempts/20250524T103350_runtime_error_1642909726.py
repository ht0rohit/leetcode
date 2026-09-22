class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while i < (len(nums) - 1) and j < len(nums) and i < j:
            if nums[j] == nums[i]:
                while nums[j] == nums[i]:
                    j += 1
                temp = nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = temp
            i += 1
            j += 1
        
        return i+1
