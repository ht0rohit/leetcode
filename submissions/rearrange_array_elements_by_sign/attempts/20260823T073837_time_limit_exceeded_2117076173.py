class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i, j = 0, 1
        flag = 1
        while j < n:

            while (flag and nums[i] < 0) or (not flag and nums[i] > 0):
                if (flag and nums[j] > 0) or (not flag and nums[j] < 0):
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

            i += 1
            j = i + 1
            
            flag = 0 if flag else 1

        return nums
