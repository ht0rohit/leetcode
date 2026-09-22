class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        
        i, j = 0, l - 1
        while i < j:
            mid = i + (j - i) // 2

            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                if nums[i] == nums[j]:
                    i += 1
                    j -= 1
                elif nums[i] < nums[j]:
                    break
                elif nums[i] > nums[j]:
                    j = mid
            
        return nums[i]